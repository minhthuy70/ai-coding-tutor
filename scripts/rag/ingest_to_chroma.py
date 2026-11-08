"""
Vector Ingestion Script for ChromaDB
Author: AI Coding Tutor Team
Description:
    Nạp toàn bộ chunks từ `data/06_rag_dataset/chunks/all_chunks.json` vào ChromaDB.
    Hỗ trợ nhúng Cosine Distance, lưu trữ Persistent và lập chỉ mục Metadata.
"""

import os
import sys
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("ChromaIngest")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
CHUNKS_FILE = BASE_DIR / "data" / "06_rag_dataset" / "chunks" / "all_chunks.json"
CHROMA_DIR = BASE_DIR / "backend" / "chroma_data"
COLLECTION_NAME = "coding_tutor_knowledge"

def run_ingestion():
    logger.info("=== BẮT ĐẦU NẠP DỮ LIỆU VÀO CHROMADB ===")
    
    if not CHUNKS_FILE.exists():
        logger.error(f"Không tìm thấy file chunks: {CHUNKS_FILE}. Vui lòng chạy chunking_engine.py trước!")
        return

    try:
        import chromadb
        from chromadb.utils import embedding_functions
    except ImportError:
        logger.error("Chưa cài đặt thư viện 'chromadb'. Vui lòng chạy: pip install chromadb")
        return

    with open(CHUNKS_FILE, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    if not chunks:
        logger.warning("File chunks rỗng!")
        return

    logger.info(f"Tổng số chunks cần nhúng: {len(chunks)}")
    CHROMA_DIR.mkdir(parents=True, exist_ok=True)

    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    
    # Sử dụng embedding function mặc định của ChromaDB (all-MiniLM-L6-v2 chạy local nhẹ và nhanh)
    emb_fn = embedding_functions.DefaultEmbeddingFunction()

    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=emb_fn,
        metadata={"hnsw:space": "cosine"}
    )

    BATCH_SIZE = 100
    total_added = 0

    for i in range(0, len(chunks), BATCH_SIZE):
        batch = chunks[i:i + BATCH_SIZE]
        ids = [item["id"] for item in batch]
        documents = [item["text"] for item in batch]
        metadatas = [item["metadata"] for item in batch]

        collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )
        total_added += len(batch)
        logger.info(f"-> Đã nạp {total_added}/{len(chunks)} chunks vào collection '{COLLECTION_NAME}'")

    logger.info(f"🎉 HOÀN TẤT NẠP CHROMADB: Đã lập chỉ mục {total_added} tài liệu tri thức tại {CHROMA_DIR}")

if __name__ == "__main__":
    run_ingestion()

