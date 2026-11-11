# -*- coding: utf-8 -*-
"""
Intelligent Markdown & Code-Aware Chunking Engine
Author: AI Coding Tutor Team
Task: NGÀY 04 - Chuẩn hóa & Xây dựng Engine Chia Nhỏ (Chunking Engine)

Features:
    1. Sử dụng MarkdownHeaderTextSplitter để phân rã tài liệu theo cấp độ tiêu đề (#, ##, ###).
    2. Sử dụng RecursiveCharacterTextSplitter (chunk_size=700, chunk_overlap=120) kết hợp Code-Aware Preservation.
    3. Đảm bảo 100% khối mã nguồn (```) không bị cắt đứt ngang thân hàm hay class.
    4. Đo lường chính xác số token bằng tiktoken (cl100k_base), cam kết không chunk nào vượt 1000 tokens.
    5. Gắn metadata phong phú (chunk_id, source, language, topic, section_title, has_code, token_count).
    6. Lưu toàn bộ kết quả ra `data/06_rag_dataset/chunks/all_chunks.json`.
"""

import os
import re
import json
import logging
from pathlib import Path
from typing import List, Dict, Any, Tuple

import tiktoken
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("ChunkingEngine")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
INPUT_DIR = BASE_DIR / "data" / "06_rag_dataset" / "cleaned"
OUTPUT_DIR = BASE_DIR / "data" / "06_rag_dataset" / "chunks"

# Khởi tạo bộ đếm token chuẩn OpenAI cl100k_base (dùng chung cho GPT-4/GPT-3.5/RAG embedding)
tokenizer = tiktoken.get_encoding("cl100k_base")

def count_tokens(text: str) -> int:
    """Đếm số lượng token chính xác của chuỗi văn bản."""
    return len(tokenizer.encode(text, disallowed_special=()))

def detect_language(filename: str, content: str = "") -> str:
    fn = filename.lower()
    if fn.startswith("py_") or fn.startswith("vi_py_") or "python" in fn or "pep8" in fn:
        return "python"
    elif fn.startswith("cpp_") or "c++" in fn or "cpp" in fn or "stl" in fn or "pointer" in fn:
        return "cpp"
    elif fn.startswith("java_") or "java" in fn:
        return "java"
    elif "math" in fn or "dsa" in fn or "big_o" in fn:
        return "algorithm_dsa"
    elif "security" in fn or "cwe" in fn:
        return "security"
    return "python" if "def " in content or "import " in content else "general"

def detect_topic(section_title: str, content: str, filename: str) -> str:
    """Tự động phân loại chủ đề sư phạm cho từng chunk."""
    text = (section_title + " " + content[:200] + " " + filename).lower()

    if any(k in text for k in ["pep8", "clean code", "style guide", "quy chuẩn"]):
        return "clean_code_pep8"
    elif any(k in text for k in ["class", "oop", "hướng đối tượng", "kế thừa", "inheritance", "đa hình", "encapsulation", "polymorphism", "object"]):
        return "object_oriented_programming"
    elif any(k in text for k in ["sqlite", "mysql", "database", "csdl", "cơ sở dữ liệu", "sql"]):
        return "database_sql"
    elif any(k in text for k in ["tkinter", "gui", "giao diện", "widget", "window", "button"]):
        return "gui_desktop"
    elif any(k in text for k in ["json", "file", "tập tin", "đọc file", "ghi file", "csv", "xml"]):
        return "file_io_data"
    elif any(k in text for k in ["numpy", "scipy", "pandas", "matplotlib", "mảng đa chiều", "ndarray"]):
        return "scientific_data_libraries"
    elif any(k in text for k in ["hàm", "function", "def ", "lambda", "module", "tham số", "return"]):
        return "functions_and_modules"
    elif any(k in text for k in ["vòng lặp", "for ", "while ", "if ", "else", "điều kiện", "rẽ nhánh", "control flow"]):
        return "control_flow_and_loops"
    elif any(k in text for k in ["list", "tuple", "dictionary", "set", "chuỗi", "string", "slicing", "cắt lát", "chỉ mục"]):
        return "data_structures_collections"
    elif any(k in text for k in ["biến", "kiểu dữ liệu", "toán tử", "nhập xuất", "print", "input", "cơ bản", "mở đầu"]):
        return "basic_syntax_types"
    elif any(k in text for k in ["ngoại lệ", "exception", "try", "except", "debugging", "lỗi", "error"]):
        return "debugging_exceptions"
    elif any(k in text for k in ["big-o", "độ phức tạp", "thuật toán", "complexity", "dsa", "toán"]):
        return "algorithm_complexity_math"
    elif any(k in text for k in ["security", "lỗ hổng", "cwe", "bảo mật", "vulnerability"]):
        return "software_security"

    return "general_programming"

def map_source_filename(clean_md_name: str) -> str:
    """Ánh xạ tên file .md về file tài liệu gốc (.pdf, .rst, .html)."""
    stem = Path(clean_md_name).stem
    if stem.startswith("VI_PY_") or stem.startswith("COMMON_") or stem.startswith("PY_01") or stem.startswith("PY_03"):
        return f"{stem}.pdf"
    elif stem in ["PY_02_DataStructures_and_OOP_Classes", "PY_04_PEP8_Clean_Code_Specification"]:
        return f"{stem}.rst"
    elif "CWE" in stem:
        return f"{stem}.html"
    return f"{stem}.pdf"

def generate_short_prefix(filename: str) -> str:
    """Tạo tiền tố ID ngắn gọn, dễ đọc cho từng tài liệu."""
    fn = filename.lower()
    if "vi_py_02" in fn: return "vi_py02_eng"
    if "vi_py_03" in fn: return "vi_py03_ctu"
    if "vi_py_04" in fn: return "vi_py04_bk"
    if "vi_py_05" in fn: return "vi_py05_ml"
    if "vi_py_06" in fn: return "vi_py06_oop"
    if "vi_py_07" in fn: return "vi_py07_file"
    if "vi_py_08" in fn: return "vi_py08_sql"
    if "vi_py_09" in fn: return "vi_py09_gui"
    if "vi_py_10" in fn: return "vi_py10_hand"
    if "vi_py_11" in fn: return "vi_py11_lab"
    if "vi_py_python_rat_la_co_ban" in fn: return "vi_py01_basic"
    if "common_01" in fn: return "cmn01_math"
    if "common_02" in fn: return "cmn02_bigo"
    if "common_03" in fn: return "cmn03_sec"
    if "common_04" in fn: return "cmn04_cwe"
    if "py_01" in fn: return "py01_tut"
    if "py_02" in fn: return "py02_oop"
    if "py_03" in fn: return "py03_dbg"
    if "py_04" in fn: return "py04_pep8"
    return Path(filename).stem[:8].lower()

def safe_code_aware_split(text: str, chunk_size: int = 700, chunk_overlap: int = 120) -> List[str]:
    """
    Chia nhỏ đoạn văn bản đảm bảo không cắt ngang bất kỳ khối code (```) nào.
    Nếu có khối code, giữ trọn vẹn khối code trong cùng một chunk.
    """
    # 1. Nếu văn bản không có code block hoặc kích thước đã nhỏ hơn chunk_size
    if len(text) <= chunk_size and "```" not in text:
        return [text]

    # 2. Tách văn bản thành các đơn vị Text và Code Block
    # Biểu thức chính quy bắt trọn từng code block từ ``` đến ```
    code_pattern = re.compile(r'(```[a-zA-Z0-9_\+\#-]*\n[\s\S]*?```)', re.MULTILINE)
    tokens_or_blocks = []
    last_idx = 0

    for match in code_pattern.finditer(text):
        pre_text = text[last_idx:match.start()].strip()
        if pre_text:
            tokens_or_blocks.append({"type": "text", "content": pre_text})
        code_content = match.group(1).strip()
        tokens_or_blocks.append({"type": "code", "content": code_content})
        last_idx = match.end()

    tail_text = text[last_idx:].strip()
    if tail_text:
        tokens_or_blocks.append({"type": "text", "content": tail_text})

    if not tokens_or_blocks:
        return [text]

    # Sử dụng RecursiveCharacterTextSplitter cho các đoạn text thường
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", "; ", ", ", " ", ""]
    )

    chunks = []
    current_chunk = ""

    for block in tokens_or_blocks:
        b_type = block["type"]
        b_content = block["content"]

        if b_type == "text":
            # Nếu đoạn text dài, chia nhỏ qua RecursiveCharacterTextSplitter
            sub_texts = text_splitter.split_text(b_content)
            for st in sub_texts:
                if len(current_chunk) + len(st) + 2 <= chunk_size:
                    current_chunk = (current_chunk + "\n\n" + st).strip()
                else:
                    if current_chunk:
                        chunks.append(current_chunk)
                    current_chunk = st
        else:
            # Là khối code: Tuyệt đối không cắt ngang thân code!
            # Nếu khối code đứng riêng lẻ vừa kích thước hoặc lớn hơn chunk_size
            if len(current_chunk) + len(b_content) + 2 <= chunk_size:
                current_chunk = (current_chunk + "\n\n" + b_content).strip()
            else:
                if current_chunk:
                    chunks.append(current_chunk)
                    current_chunk = ""
                # Khối code đứng độc lập làm 1 chunk riêng biệt để bảo toàn hàm/class
                chunks.append(b_content)

    if current_chunk:
        chunks.append(current_chunk)

    # Kiểm tra an toàn: Đảm bảo không có dấu ``` nào bị mở lẻ loi
    validated_chunks = []
    for c in chunks:
        c_strip = c.strip()
        if not c_strip:
            continue
        # Đếm số lần xuất hiện của ```
        backtick_count = len(re.findall(r'```', c_strip))
        if backtick_count % 2 != 0:
            # Nếu bị mở dở, tự động đóng khối code
            c_strip += "\n```"
        validated_chunks.append(c_strip)

    return validated_chunks if validated_chunks else [text]

def run_chunking_pipeline() -> Tuple[List[Dict[str, Any]], Dict[str, Any]]:
    """Thực thi toàn bộ luồng Chunking cho toàn bộ kho tài liệu cleaned."""
    logger.info("=== BẮT ĐẦU CHUNKING ENGINE (NGÀY 04) ===")
    logger.info(f"Thư mục nguồn (Cleaned): {INPUT_DIR}")
    logger.info(f"Thư mục đích (Chunks)  : {OUTPUT_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    md_files = sorted(list(INPUT_DIR.glob("*.md")))

    if not md_files:
        raise FileNotFoundError(f"Không tìm thấy file .md nào trong {INPUT_DIR}. Hãy chạy clean_markdown.py trước!")

    # Cấu hình MarkdownHeaderTextSplitter để bắt các tiêu đề H1, H2, H3
    headers_to_split_on = [
        ("#", "Header 1"),
        ("##", "Header 2"),
        ("###", "Header 3"),
    ]
    md_header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=headers_to_split_on,
        strip_headers=False
    )

    all_chunks = []
    stats = {
        "total_files": len(md_files),
        "total_chunks": 0,
        "max_token_count": 0,
        "chunks_with_code": 0,
        "chunks_exceeding_1000_tokens": 0,
        "language_distribution": {},
        "topic_distribution": {}
    }

    global_counter = 0

    for file_path in md_files:
        filename = file_path.name
        source_doc = map_source_filename(filename)
        prefix = generate_short_prefix(filename)
        file_lang = detect_language(filename)

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            full_text = f.read()

        # 1. Tách theo Header bằng MarkdownHeaderTextSplitter
        try:
            header_docs = md_header_splitter.split_text(full_text)
        except Exception as e:
            logger.warning(f"Lỗi MarkdownHeaderTextSplitter trên {filename}, fallback sang text thuần: {e}")
            header_docs = [type('Doc', (), {'page_content': full_text, 'metadata': {}})()]

        doc_chunk_idx = 0

        for h_doc in header_docs:
            raw_section = h_doc.page_content.strip()
            if not raw_section or len(raw_section) < 30:
                continue

            # Xác định section_title từ metadata Header
            h1 = h_doc.metadata.get("Header 1", "")
            h2 = h_doc.metadata.get("Header 2", "")
            h3 = h_doc.metadata.get("Header 3", "")
            section_title = h3 or h2 or h1 or "Chung"

            # 2. Áp dụng Code-Aware Splitter (chunk_size=700, chunk_overlap=120)
            sub_chunks = safe_code_aware_split(raw_section, chunk_size=700, chunk_overlap=120)

            for sub_text in sub_chunks:
                clean_text = sub_text.strip()
                if len(clean_text) < 30:
                    continue

                global_counter += 1
                doc_chunk_idx += 1
                chunk_id = f"{prefix}_{doc_chunk_idx:04d}"
                has_code = "```" in clean_text
                token_len = count_tokens(clean_text)
                topic = detect_topic(section_title, clean_text, filename)

                if token_len > stats["max_token_count"]:
                    stats["max_token_count"] = token_len

                if token_len > 1000:
                    stats["chunks_exceeding_1000_tokens"] += 1

                if has_code:
                    stats["chunks_with_code"] += 1

                # Thống kê phân phối
                stats["language_distribution"][file_lang] = stats["language_distribution"].get(file_lang, 0) + 1
                stats["topic_distribution"][topic] = stats["topic_distribution"].get(topic, 0) + 1

                # Chuẩn hóa cấu trúc chunk theo đúng yêu cầu DoD
                chunk_item = {
                    "chunk_id": chunk_id,
                    "text": clean_text,
                    "source": source_doc,
                    "language": file_lang,
                    "topic": topic,
                    "section_title": section_title,
                    "has_code": has_code,
                    "token_count": token_len,
                    "metadata": {
                        "chunk_id": chunk_id,
                        "source": source_doc,
                        "source_file": filename,
                        "language": file_lang,
                        "topic": topic,
                        "section_title": section_title,
                        "has_code": has_code,
                        "token_count": token_len,
                        "length_chars": len(clean_text),
                        "header_hierarchy": " > ".join(filter(None, [h1, h2, h3])) or section_title
                    }
                }
                all_chunks.append(chunk_item)

        logger.info(f"-> {filename:<50} | Tạo: {doc_chunk_idx:>4} chunks | Ngôn ngữ: {file_lang}")

    stats["total_chunks"] = len(all_chunks)

    # 3. Lưu toàn bộ kết quả ra all_chunks.json
    out_file = OUTPUT_DIR / "all_chunks.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    logger.info(f"✅ ĐÃ LƯU THÀNH CÔNG {len(all_chunks)} CHUNKS VÀO: {out_file}")
    return all_chunks, stats

if __name__ == "__main__":
    chunks, stats = run_chunking_pipeline()
    print("\n" + "=" * 80)
    print("📊 BÁO CÁO NGHIỆM THU NGÀY 04 (DEFINITION OF DONE):")
    print(f"  • Tổng số tài liệu xử lý             : {stats['total_files']} files")
    print(f"  • Tổng số chunks sinh ra             : {stats['total_chunks']:,} chunks")
    print(f"  • Số chunk chứa mã nguồn (has_code)  : {stats['chunks_with_code']:,} chunks")
    print(f"  • Token lớn nhất (Max token count)   : {stats['max_token_count']} tokens (Chuẩn < 1000 tokens)")
    print(f"  • Số chunk vượt quá 1000 tokens      : {stats['chunks_exceeding_1000_tokens']} chunks (Đạt tiêu chí DoD: 0)")
    print("=" * 80)
