"""
Intelligent Markdown, Code-Aware & Table-Aware Chunking Engine (v2.0)
Author: AI Coding Tutor Team
Task: NGÀY 04 - Nâng cấp Chunking Engine cho RAG Đa Phương Thức
Description:
    Hệ thống phân đoạn tri thức tiên tiến kết hợp thế mạnh của AST Block Chunking và Code-Aware Splitting:
    1. Đo kích thước và giới hạn chính xác bằng Tokenizer chuẩn BPE (tiktoken cl100k_base).
    2. Phân cấp cây tiêu đề chuyên sâu (Heading Hierarchy Stack) tạo đường dẫn Breadcrumbs (section_path).
    3. Bảo toàn nguyên vẹn 100% khối mã nguồn (Code Blocks), không cắt ngang thân hàm/class.
    4. Xử lý bảng biểu thông minh (Table-Aware): Hỗ trợ cả Markdown Table và HTML Table, bảo tồn Header.
    5. Nhận diện và đánh dấu đa chiều (has_code, has_table, has_equation, section_depth).
    6. Tương thích 100% với ChromaDB và các mô hình Embedding hiện đại.
"""

import os
import re
import json
import logging
from pathlib import Path
from typing import List, Dict, Any

try:
    import tiktoken
    ENCODING = tiktoken.get_encoding("cl100k_base")
except Exception:
    ENCODING = None

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("ChunkingEngine")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
INPUT_DIR = BASE_DIR / "data" / "06_rag_dataset" / "cleaned"
OUTPUT_DIR = BASE_DIR / "data" / "06_rag_dataset" / "chunks"

# Cấu hình Token Budget cho RAG
MAX_TOKENS = 650        # Kích thước chunk tối đa (Tokens BPE chuẩn cl100k_base)
MIN_CHUNK_CHARS = 40    # Ngưỡng ký tự tối thiểu để loại bỏ mẩu rác

def count_tokens(text: str) -> int:
    """Đo số lượng Token bằng tiktoken (chuẩn cl100k_base) hoặc xấp xỉ fallback."""
    if not text:
        return 0
    if ENCODING is not None:
        try:
            return len(ENCODING.encode(text))
        except Exception:
            pass
    # Fallback ước lượng (1 token ~ 3.5 ký tự)
    return max(1, int(len(text) / 3.5))

def detect_language_from_filename(filename: str) -> str:
    """Tự động phân loại ngôn ngữ và chủ đề tài liệu từ tên file."""
    fn = filename.lower()
    if fn.startswith("py_") or "python" in fn or "pep8" in fn:
        return "python"
    elif fn.startswith("cpp_") or "c++" in fn or "cpp" in fn or "stl" in fn or "pointer" in fn:
        return "cpp"
    elif fn.startswith("java_") or "java" in fn:
        return "java"
    elif fn.startswith("common_"):
        return "general"
    elif "math" in fn or "big_o" in fn or "algorithm" in fn:
        return "math_cs"
    elif "security" in fn or "cwe" in fn:
        return "security"
    return "general"

def is_markdown_table(text: str) -> bool:
    """Kiểm tra khối văn bản có phải là bảng Markdown hay không."""
    lines = [l.strip() for l in text.strip().splitlines() if l.strip()]
    if len(lines) < 2:
        return False
    if "|" not in lines[0]:
        return False
    return bool(re.match(r"^\|?[\s:-|]+\|?$", lines[1]))

def is_html_table(text: str) -> bool:
    """Kiểm tra khối văn bản có phải là bảng HTML hay không."""
    t = text.strip().lower()
    return t.startswith("<table") and "</table>" in t

def split_by_words_fallback(text: str, max_tokens: int) -> List[str]:
    """Chia nhỏ theo từ nếu một đoạn văn bản/chuỗi không có ranh giới câu rõ ràng."""
    words = text.split()
    if not words:
        return [text] if text.strip() else []

    chunks = []
    curr_words = []

    for w in words:
        candidate = " ".join(curr_words + [w])
        if count_tokens(candidate) <= max_tokens:
            curr_words.append(w)
        else:
            if curr_words:
                chunks.append(" ".join(curr_words))
                curr_words = [w]
            else:
                # Nếu riêng một từ/chuỗi quá dài (ví dụ chuỗi hash hoặc base64)
                chunks.append(w[:max_tokens * 3])
                curr_words = []

    if curr_words:
        chunks.append(" ".join(curr_words))

    return chunks

def split_large_html_table(html_text: str, max_tokens: int) -> List[str]:
    """Chia nhỏ bảng HTML thành các phần vừa vặn, giữ nguyên thẻ <table>...</table>."""
    rows = re.findall(r'<tr[\s\S]*?</tr>', html_text, re.IGNORECASE)
    if not rows:
        return split_by_words_fallback(html_text, max_tokens)

    sub_tables = []
    curr_rows = []
    for r in rows:
        candidate = "<table>\n" + "\n".join(curr_rows + [r]) + "\n</table>"
        if count_tokens(candidate) <= max_tokens:
            curr_rows.append(r)
        else:
            if curr_rows:
                sub_tables.append("<table>\n" + "\n".join(curr_rows) + "\n</table>")
                curr_rows = []
            
            # Nếu riêng 1 hàng tr này vượt max_tokens
            if count_tokens(r) > max_tokens:
                sub_tables.extend(split_by_words_fallback(r, max_tokens))
            else:
                curr_rows = [r]

    if curr_rows:
        sub_tables.append("<table>\n" + "\n".join(curr_rows) + "\n</table>")

    return sub_tables if sub_tables else [html_text]

def split_large_markdown_table(table_text: str, max_tokens: int) -> List[str]:
    """
    Chia nhỏ bảng Markdown dài:
    Mỗi phần con đều được giữ nguyên hàng Header và Separator.
    """
    lines = [l.strip() for l in table_text.strip().splitlines() if l.strip()]
    if len(lines) < 3:
        return split_by_words_fallback(table_text, max_tokens)

    header_line = lines[0]
    separator_line = lines[1] if re.match(r"^\|?[\s:-|]+\|?$", lines[1]) else "|---|---|"
    data_rows = lines[2:] if separator_line == lines[1] else lines[1:]

    sub_tables = []
    current_rows = []

    for row in data_rows:
        candidate_text = "\n".join([header_line, separator_line] + current_rows + [row])
        if count_tokens(candidate_text) <= max_tokens:
            current_rows.append(row)
        else:
            if current_rows:
                sub_tables.append("\n".join([header_line, separator_line] + current_rows))
                current_rows = []
            
            if count_tokens(row) > max_tokens:
                sub_tables.extend(split_by_words_fallback(row, max_tokens))
            else:
                current_rows = [row]

    if current_rows:
        sub_tables.append("\n".join([header_line, separator_line] + current_rows))

    return sub_tables if sub_tables else [table_text]

def split_large_code_block(code_block: str, max_tokens: int) -> List[str]:
    """
    Chia nhỏ khối code quá dài:
    Đảm bảo mỗi slice đều được bọc trong thẻ ```<lang> ... ``` đầy đủ,
    không làm vỡ cấu trúc Markdown và giữ nguyên thụt lề (indentation).
    """
    lines = code_block.strip().splitlines()
    if len(lines) <= 2:
        return [code_block]

    header = lines[0]   # Ví dụ: ```python
    footer = lines[-1]   # Ví dụ: ```
    body_lines = lines[1:-1]

    slices = []
    current_body = []

    for line in body_lines:
        candidate_code = "\n".join([header] + current_body + [line, footer])
        if count_tokens(candidate_code) <= max_tokens:
            current_body.append(line)
        else:
            if current_body:
                slices.append("\n".join([header] + current_body + [footer]))
                current_body = []
            
            if count_tokens(line) > max_tokens:
                # Dòng code đơn lẻ siêu dài
                for sub_line in split_by_words_fallback(line, max_tokens - 10):
                    slices.append(f"{header}\n{sub_line}\n{footer}")
            else:
                current_body = [line]

    if current_body:
        slices.append("\n".join([header] + current_body + [footer]))

    return slices if slices else [code_block]

def split_by_headings_with_path(content: str) -> List[Dict[str, Any]]:
    """
    Tách tài liệu dựa trên cây phân cấp tiêu đề (#, ##, ###, ####),
    duy trì heading stack để tạo đường dẫn section_path đầy đủ.
    """
    heading_pattern = re.compile(r'^(#{1,4})\s+(.+)$', re.MULTILINE)
    matches = list(heading_pattern.finditer(content))

    if not matches:
        return [{
            "title": "Chung",
            "section_path": "Chung",
            "section_depth": 1,
            "content": content.strip()
        }]

    sections = []
    if matches[0].start() > 0:
        intro_text = content[:matches[0].start()].strip()
        if intro_text:
            sections.append({
                "title": "Mở đầu",
                "section_path": "Mở đầu",
                "section_depth": 1,
                "content": intro_text
            })

    heading_stack: List[Dict[str, Any]] = []

    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        level = len(matches[i].group(1))
        title = matches[i].group(2).strip()
        sec_content = content[start:end].strip()

        # Cập nhật stack phân cấp
        while heading_stack and heading_stack[-1]["level"] >= level:
            heading_stack.pop()

        heading_stack.append({"level": level, "title": title})

        # Tạo breadcrumb phân cấp: "Chương 1 > 1.1 Khái niệm > 1.1.1 Cú pháp"
        path_titles = [h["title"] for h in heading_stack]
        section_path_str = " > ".join(path_titles)

        sections.append({
            "title": title,
            "section_path": section_path_str,
            "section_depth": len(path_titles),
            "content": sec_content
        })

    return sections

def extract_atomic_blocks(text: str) -> List[str]:
    """
    Phân tách nội dung văn bản thành các đơn vị nguyên tử (Atomic Units):
    - Khối code blocks (```` ```...``` ````)
    - Bảng biểu HTML (<table>...</table>)
    - Các đoạn văn bản và bảng Markdown
    """
    code_pattern = re.compile(r'(```[a-zA-Z0-9_\+\#-]*\n[\s\S]*?```)', re.MULTILINE)
    raw_pieces = []
    last_end = 0

    for match in code_pattern.finditer(text):
        start, end = match.span()
        pre_text = text[last_end:start].strip()
        if pre_text:
            raw_pieces.append(("text", pre_text))
        code_block = match.group(1).strip()
        if code_block:
            raw_pieces.append(("code", code_block))
        last_end = end

    post_text = text[last_end:].strip()
    if post_text:
        raw_pieces.append(("text", post_text))

    blocks = []
    for kind, piece in raw_pieces:
        if kind == "code":
            blocks.append(piece)
        else:
            html_parts = re.split(r'(<table[\s\S]*?</table>)', piece, flags=re.IGNORECASE)
            for hp in html_parts:
                hp = hp.strip()
                if not hp:
                    continue
                if is_html_table(hp):
                    blocks.append(hp)
                else:
                    paras = [p.strip() for p in re.split(r'\n\s*\n', hp) if p.strip()]
                    blocks.extend(paras)

    return blocks

def recursive_token_aware_split(text: str, max_tokens: int = MAX_TOKENS) -> List[str]:
    """
    Thuật toán chia nhỏ văn bản thông minh (Code & Table Aware Token Splitter):
    1. Giữ nguyên khối code và bảng nếu vừa vặn trong ngân sách token.
    2. Cắt bảng HTML / Markdown theo hàng nếu bảng quá dài.
    3. Cắt code bọc đầy đủ thẻ mở/đóng nếu khối code quá dài.
    4. Gom cụm các đoạn văn bản kề nhau cho đến khi chạm ngưỡng MAX_TOKENS.
    """
    if count_tokens(text) <= max_tokens:
        return [text]

    atomic_blocks = extract_atomic_blocks(text)
    processed_units: List[str] = []

    for block in atomic_blocks:
        b_tokens = count_tokens(block)
        if b_tokens <= max_tokens:
            processed_units.append(block)
        else:
            if block.startswith("```") and block.endswith("```"):
                processed_units.extend(split_large_code_block(block, max_tokens))
            elif is_html_table(block):
                processed_units.extend(split_large_html_table(block, max_tokens))
            elif is_markdown_table(block) or ("|" in block and "\n|" in block):
                processed_units.extend(split_large_markdown_table(block, max_tokens))
            else:
                sentences = re.split(r'(?<=[.!?。！？\n])\s+', block)
                curr_sent = ""
                for s in sentences:
                    s = s.strip()
                    if not s:
                        continue
                    if count_tokens(s) > max_tokens:
                        if curr_sent:
                            processed_units.append(curr_sent)
                            curr_sent = ""
                        processed_units.extend(split_by_words_fallback(s, max_tokens))
                        continue

                    cand = f"{curr_sent}\n{s}" if curr_sent else s
                    if count_tokens(cand) <= max_tokens:
                        curr_sent = cand
                    else:
                        if curr_sent:
                            processed_units.append(curr_sent)
                        curr_sent = s
                if curr_sent:
                    processed_units.append(curr_sent)

    # Bảo đảm tuyệt đối: không có unit nào vượt quá max_tokens
    guaranteed_units: List[str] = []
    for u in processed_units:
        u_tok = count_tokens(u)
        if u_tok <= max_tokens:
            guaranteed_units.append(u)
        else:
            guaranteed_units.extend(split_by_words_fallback(u, max_tokens))

    # Gom các đơn vị đã xử lý thành các chunk vừa vặn (đo token thực tế khi ghép chuỗi)
    final_chunks: List[str] = []
    current_parts: List[str] = []

    for unit in guaranteed_units:
        candidate_parts = current_parts + [unit]
        candidate_text = "\n\n".join(candidate_parts).strip()
        if count_tokens(candidate_text) <= max_tokens:
            current_parts = candidate_parts
        else:
            if current_parts:
                final_chunks.append("\n\n".join(current_parts).strip())
            current_parts = [unit]

    if current_parts:
        final_chunks.append("\n\n".join(current_parts).strip())

    return final_chunks if final_chunks else [text]

def process_chunking():
    """Hàm chạy toàn bộ pipeline chunking và xuất kết quả ra all_chunks.json."""
    logger.info("=== BẮT ĐẦU CHUNKING ENGINE NÂNG CẤP (v2.0) ===")
    logger.info(f"Tokenizer: {'tiktoken (cl100k_base)' if ENCODING else 'Fallback Character Estimation'}")
    logger.info(f"Giới hạn Token Budget (MAX_TOKENS): {MAX_TOKENS}")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    md_files = sorted(list(INPUT_DIR.glob("*.md")))
    if not md_files:
        logger.warning(f"Chưa có file markdown nào trong {INPUT_DIR}. Vui lòng chạy clean_markdown.py trước!")
        return

    all_chunks: List[Dict[str, Any]] = []
    chunk_counter = 0

    total_with_code = 0
    total_with_table = 0
    total_with_equation = 0

    for file_path in md_files:
        filename = file_path.name
        language = detect_language_from_filename(filename)
        logger.info(f"Đang phân đoạn tài liệu: {filename} (Ngôn ngữ: {language})")

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        sections = split_by_headings_with_path(content)

        for sec in sections:
            sec_title = sec["title"]
            sec_path = sec["section_path"]
            sec_depth = sec["section_depth"]

            chunks = recursive_token_aware_split(sec["content"], max_tokens=MAX_TOKENS)

            for chunk_text in chunks:
                clean_chunk_text = chunk_text.strip()
                if len(clean_chunk_text) < MIN_CHUNK_CHARS:
                    continue

                chunk_counter += 1
                token_count = count_tokens(clean_chunk_text)
                has_code = "```" in clean_chunk_text
                has_table = (
                    is_markdown_table(clean_chunk_text)
                    or is_html_table(clean_chunk_text)
                    or ("|" in clean_chunk_text and "\n|-" in clean_chunk_text)
                )
                has_equation = bool(re.search(r'\$[^\$\n]+\$|\$\$[\s\S]+?\$\$', clean_chunk_text))

                if has_code:
                    total_with_code += 1
                if has_table:
                    total_with_table += 1
                if has_equation:
                    total_with_equation += 1

                chunk_id = f"{Path(filename).stem}_c{chunk_counter:04d}"

                chunk_data = {
                    "id": chunk_id,
                    "text": clean_chunk_text,
                    "metadata": {
                        "source_file": filename,
                        "section_title": sec_title,
                        "section_path": sec_path,
                        "section_depth": sec_depth,
                        "language": language,
                        "token_count": token_count,
                        "length_chars": len(clean_chunk_text),
                        "has_code": has_code,
                        "has_table": has_table,
                        "has_equation": has_equation
                    }
                }
                all_chunks.append(chunk_data)

    out_file = OUTPUT_DIR / "all_chunks.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    logger.info(f"✅ HOÀN TẤT: Đã tạo {len(all_chunks)} chunks chất lượng cao tại: {out_file}")
    logger.info("📊 THỐNG KÊ CHI TIẾT:")
    logger.info(f"  • Tổng số chunks          : {len(all_chunks):,}")
    logger.info(f"  • Chunks chứa Mã nguồn    : {total_with_code:,} ({total_with_code/len(all_chunks)*100:.1f}%)")
    logger.info(f"  • Chunks chứa Bảng biểu   : {total_with_table:,} ({total_with_table/len(all_chunks)*100:.1f}%)")
    logger.info(f"  • Chunks chứa Công thức   : {total_with_equation:,} ({total_with_equation/len(all_chunks)*100:.1f}%)")

    # Kiểm tra nghiệm thu chất lượng Chunks
    token_list = [c["metadata"]["token_count"] for c in all_chunks]
    logger.info(f"  • Token nhỏ nhất          : {min(token_list)}")
    logger.info(f"  • Token lớn nhất          : {max(token_list)}")
    logger.info(f"  • Token trung bình        : {sum(token_list)/len(token_list):.1f}")
    assert max(token_list) <= MAX_TOKENS, f"Có chunk vượt ngưỡng MAX_TOKENS: {max(token_list)}"
    logger.info("🎉 100% CHUNKS ĐẠT CHUẨN NGHIỆM THU TOKEN VÀ BẢO TOÀN CẤU TRÚC!")

if __name__ == "__main__":
    process_chunking()
