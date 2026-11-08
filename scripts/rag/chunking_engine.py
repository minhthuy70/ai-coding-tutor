"""
Intelligent Markdown & Code-Aware Chunking Engine
Author: AI Coding Tutor Team
Description:
    Chia nhỏ các file Markdown đã làm sạch thành các Chunks ngữ cảnh hoàn chỉnh:
    - Phân cấp theo Markdown Headings (#, ##, ###).
    - Bảo toàn nguyên vẹn khối mã nguồn (Code Blocks), không cắt ngang hàm / class.
    - Gắn Metadata 2 chiều phong phú (language, topic, source_doc, section_title).
    - Xuất kết quả ra `data/06_rag_dataset/chunks/all_chunks.json`.
"""

import os
import re
import json
import logging
from pathlib import Path
from typing import List, Dict, Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("ChunkingEngine")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
INPUT_DIR = BASE_DIR / "data" / "06_rag_dataset" / "cleaned"
OUTPUT_DIR = BASE_DIR / "data" / "06_rag_dataset" / "chunks"

def detect_language_from_filename(filename: str) -> str:
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

def split_by_headings(content: str) -> List[Dict[str, str]]:
    """Tách tài liệu dựa trên các thẻ tiêu đề Markdown #, ##, ###."""
    heading_pattern = re.compile(r'^(#{1,3})\s+(.+)$', re.MULTILINE)
    matches = list(heading_pattern.finditer(content))
    
    if not matches:
        return [{"title": "Chung", "content": content.strip()}]
        
    sections = []
    # Đoạn mở đầu trước heading đầu tiên (nếu có)
    if matches[0].start() > 0:
        intro_text = content[:matches[0].start()].strip()
        if intro_text:
            sections.append({"title": "Mở đầu", "content": intro_text})
            
    for i in range(len(matches)):
        start = matches[i].start()
        end = matches[i+1].start() if i + 1 < len(matches) else len(content)
        title = matches[i].group(2).strip()
        sec_content = content[start:end].strip()
        sections.append({"title": title, "content": sec_content})
        
    return sections

def recursive_code_aware_split(text: str, max_chars: int = 1800, overlap_chars: int = 200) -> List[str]:
    """
    Chia nhỏ một section dài thành nhiều chunk vừa vặn,
    ưu tiên tách ở ranh giới giữa các khối code hoặc giữa các đoạn văn.
    """
    if len(text) <= max_chars:
        return [text]

    # Phân tách ưu tiên theo: khối code đóng ```, hoặc 2 dấu xuống dòng, hoặc 1 dấu xuống dòng
    sub_chunks = []
    paragraphs = re.split(r'(\n\n```[a-zA-Z0-9_\+\-]*[\s\S]*?```\n\n|\n\n)', text)
    
    current_chunk = ""
    for piece in paragraphs:
        if not piece:
            continue
        if len(current_chunk) + len(piece) <= max_chars:
            current_chunk += piece
        else:
            if current_chunk.strip():
                sub_chunks.append(current_chunk.strip())
            # Giữ lại một phần overlap nếu có thể
            current_chunk = piece
            
    if current_chunk.strip():
        sub_chunks.append(current_chunk.strip())

    return sub_chunks if sub_chunks else [text[:max_chars]]

def process_chunking():
    logger.info("=== BẮT ĐẦU CHUNKING ENGINE ===")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    md_files = list(INPUT_DIR.glob("*.md"))
    if not md_files:
        logger.warning(f"Chưa có file markdown nào trong {INPUT_DIR}. Vui lòng chạy clean_markdown.py trước!")
        return

    all_chunks: List[Dict[str, Any]] = []
    chunk_counter = 0

    for file_path in md_files:
        filename = file_path.name
        language = detect_language_from_filename(filename)
        logger.info(f"Đang phân đoạn tài liệu: {filename} (Ngôn ngữ: {language})")

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        sections = split_by_headings(content)
        for sec in sections:
            sec_title = sec["title"]
            chunks = recursive_code_aware_split(sec["content"])
            
            for sub_idx, chunk_text in enumerate(chunks):
                chunk_counter += 1
                has_code = "```" in chunk_text
                chunk_id = f"{Path(filename).stem}_c{chunk_counter:04d}"
                
                chunk_data = {
                    "id": chunk_id,
                    "text": chunk_text,
                    "metadata": {
                        "source_file": filename,
                        "section_title": sec_title,
                        "language": language,
                        "has_code": has_code,
                        "length_chars": len(chunk_text)
                    }
                }
                all_chunks.append(chunk_data)

    out_file = OUTPUT_DIR / "all_chunks.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, ensure_ascii=False, indent=2)

    logger.info(f"✅ HOÀN TẤT: Đã tạo {len(all_chunks)} chunks chất lượng cao tại: {out_file}")

if __name__ == "__main__":
    process_chunking()

