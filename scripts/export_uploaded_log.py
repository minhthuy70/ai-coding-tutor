# -*- coding: utf-8 -*-
"""
Export and View Uploaded Chunks in ChromaDB
Author: AI Coding Tutor Team
Description:
    Trích xuất toàn bộ các đoạn tri thức (chunks) do Giảng viên nạp mới
    trong ChromaDB và ghi ra file dữ liệu:
    1. data/09_chromadb/instructor_uploaded_log.jsonl (mỗi dòng 1 bản ghi JSON)
    2. data/09_chromadb/instructor_uploaded_log.md (file Markdown dễ đọc trong VS Code)
"""

import json
import sqlite3
from pathlib import Path
from datetime import datetime
import chromadb

BASE_DIR = Path(__file__).resolve().parent.parent
CHROMA_DIR = BASE_DIR / "data" / "09_chromadb"
JSONL_LOG = CHROMA_DIR / "instructor_uploaded_log.jsonl"
MD_LOG = CHROMA_DIR / "instructor_uploaded_log.md"


def export_logs():
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    all_records = []

    for coll_name in ["qwen3_text", "jina_code"]:
        try:
            coll = client.get_collection(coll_name)
            res = coll.get(where={"source": "instructor_upload"}, include=["documents", "metadatas"])
            for cid, doc, meta in zip(res["ids"], res["documents"], res["metadatas"]):
                record = {
                    "id": cid,
                    "collection": coll_name,
                    "filename": meta.get("filename", ""),
                    "topic": meta.get("topic", ""),
                    "language": meta.get("language", "python"),
                    "chunk_index": meta.get("chunk_index", 0),
                    "total_chunks": meta.get("total_chunks", 1),
                    "created_at": meta.get("created_at", ""),
                    "content": doc
                }
                all_records.append(record)
        except Exception as e:
            print(f"Lỗi đọc collection {coll_name}: {e}")

    # Sắp xếp theo thời gian nạp
    all_records.sort(key=lambda x: x.get("created_at", ""))

    # 1. Ghi file JSONL (1 dòng = 1 record)
    with open(JSONL_LOG, "w", encoding="utf-8") as f:
        for r in all_records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # 2. Ghi file Markdown để xem trực tiếp giao diện đẹp trong VS Code
    with open(MD_LOG, "w", encoding="utf-8") as f:
        f.write("# NHẬT KÝ CÁC DÒNG TRI THỨC MỚI ĐƯỢC GIẢNG VIÊN NẠP VÀO HỆ THỐNG\n\n")
        f.write(f"> **Tổng số dòng tri thức mới**: {len(all_records)} chunks\n")
        f.write(f"> **Cập nhật lúc**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"> **Vị trí lưu trữ vật lý**: `{JSONL_LOG.relative_to(BASE_DIR)}` & `{CHROMA_DIR.relative_to(BASE_DIR)}/chroma.sqlite3`\n\n")
        f.write("---\n\n")

        for idx, r in enumerate(all_records, start=1):
            f.write(f"### Dòng {idx}: `{r['id']}`\n\n")
            f.write(f"- **Tệp nguồn (Filename)**: `{r['filename']}`\n")
            f.write(f"- **Chủ đề (Topic)**: `{r['topic']}`\n")
            f.write(f"- **Collection RAG**: `{r['collection']}` (Ngôn ngữ: `{r['language']}`)\n")
            f.write(f"- **Thời gian nạp**: `{r['created_at']}` (Chunk {r['chunk_index'] + 1}/{r['total_chunks']})\n\n")
            f.write("**Nội dung đoạn trích đã chunk & vector hóa:**\n")
            f.write("```markdown\n")
            f.write(r["content"].strip() + "\n")
            f.write("```\n\n")
            f.write("---\n\n")

    print(f" Đã xuất thành công {len(all_records)} dòng tri thức mới:")
    print(f"  1. File JSONL : {JSONL_LOG}")
    print(f"  2. File MD    : {MD_LOG}")

    # 3. Kiểm tra thông tin trong file nhị phân chroma.sqlite3
    sqlite_file = CHROMA_DIR / "chroma.sqlite3"
    if sqlite_file.exists():
        conn = sqlite3.connect(str(sqlite_file))
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM embedding_metadata WHERE key = 'source' AND string_value = 'instructor_upload'")
        count_meta = c.fetchone()[0]
        print(f"  3. Trong file SQLite gốc ({sqlite_file.name}): Tìm thấy {count_meta} bản ghi metadata 'instructor_upload'.")
        conn.close()


if __name__ == "__main__":
    export_logs()
