# -*- coding: utf-8 -*-
"""
ChromaDB Ingestion Pipeline (Production Version B)
Nạp 5,230 pre-computed vectors vào ChromaDB PersistentClient:
- Collection 1: qwen3_text (4,293 vectors, 1024-dim, cosine)
- Collection 2: jina_code (937 vectors, 768-dim, cosine)
Lưu trữ vĩnh viễn tại: data/09_chromadb/
"""

import sys
import json
import math
import time
import gc
from pathlib import Path
from unittest.mock import MagicMock

# Windows gRPC telemetry patch
if "grpc" not in sys.modules:
    try:
        import grpc
    except (ImportError, OSError):
        dummy_grpc = MagicMock()
        dummy_grpc.__version__ = "1.85.3"
        sys.modules["grpc"] = dummy_grpc
        sys.modules["grpc._compression"] = dummy_grpc
        sys.modules["grpc._cython"] = dummy_grpc
        sys.modules["grpc._cython.cygrpc"] = dummy_grpc

import chromadb

def sanitize_metadata(raw_meta: dict) -> dict:
    """Đảm bảo mọi giá trị metadata chỉ gồm str, int, float, bool."""
    clean = {}
    for k, v in raw_meta.items():
        if v is None:
            clean[k] = ""
        elif isinstance(v, (str, int, float, bool)):
            clean[k] = v
        elif isinstance(v, (list, dict)):
            clean[k] = json.dumps(v, ensure_ascii=False)
        else:
            clean[k] = str(v)
    return clean

def main():
    print("=" * 70)
    print("🚀 BẮT ĐẦU NẠP VECTORS VÀO CHROMADB (NGÀY 05 - BƯỚC 3)")
    print("=" * 70)
    start_total_time = time.time()

    # 1. Đường dẫn dữ liệu
    qwen_vector_file = Path("data/08_rag_dataset/embeddings/qwen3_text/qwen3_text_vectors.jsonl")
    jina_vector_file = Path("data/08_rag_dataset/embeddings/jina_code/jina_code_vectors.jsonl")
    all_chunks_file = Path("data/06_rag_dataset/chunks/all_chunks.json")
    db_path = Path("data/09_chromadb")
    db_path.mkdir(parents=True, exist_ok=True)

    assert qwen_vector_file.exists(), f"Không tìm thấy file: {qwen_vector_file}"
    assert jina_vector_file.exists(), f"Không tìm thấy file: {jina_vector_file}"
    assert all_chunks_file.exists(), f"Không tìm thấy file: {all_chunks_file}"

    # 2. Đọc map toàn bộ chunks từ all_chunks.json
    print(f"\n📂 Đang nạp all_chunks.json ({all_chunks_file})...")
    with open(all_chunks_file, "r", encoding="utf-8") as f:
        all_chunks_data = json.load(f)
    chunks_map = {c["id"]: c for c in all_chunks_data}
    print(f"✅ Đã nạp thành công {len(chunks_map):,} document chunks vào bộ nhớ.")
    assert len(chunks_map) == 5230, f"Kỳ vọng 5,230 chunks, thực tế: {len(chunks_map)}"

    # 3. Khởi tạo PersistentClient
    print(f"\n💾 Khởi tạo ChromaDB PersistentClient tại: {db_path.resolve()}")
    client = chromadb.PersistentClient(path=str(db_path))

    # =========================================================================
    # 4. INGESTION COLLECTION 1: qwen3_text (4,293 chunks, 1024-dim, cosine)
    # =========================================================================
    print("\n" + "-" * 70)
    print("📦 INGESTION COLLECTION 1: qwen3_text (1024-dim, Cosine HNSW)")
    print("-" * 70)
    coll_qwen_name = "qwen3_text"
    coll_qwen_dim = 1024
    coll_qwen_expected = 4293

    coll_qwen = client.get_or_create_collection(
        name=coll_qwen_name,
        metadata={"hnsw:space": "cosine", "description": "Qwen3-Embedding-0.6B 1024-dim text collection"}
    )
    print(f"  • Collection '{coll_qwen_name}' đã sẵn sàng.")

    qwen_records = []
    with open(qwen_vector_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                qwen_records.append(json.loads(line))
    print(f"  • Đã đọc {len(qwen_records):,} records từ vector Qwen3.")
    assert len(qwen_records) == coll_qwen_expected, f"Kỳ vọng {coll_qwen_expected}, có {len(qwen_records)}"

    batch_size = 250
    total_qwen_batches = math.ceil(len(qwen_records) / batch_size)
    qwen_start_time = time.time()

    for b_idx in range(total_qwen_batches):
        batch = qwen_records[b_idx * batch_size : (b_idx + 1) * batch_size]
        b_ids, b_vecs, b_docs, b_metas = [], [], [], []

        for r in batch:
            cid = r["chunk_id"]
            vec = r["vector"]
            assert len(vec) == coll_qwen_dim, f"Sai dim Qwen tại chunk {cid}: {len(vec)}"

            chunk_ref = chunks_map.get(cid, {})
            doc_text = chunk_ref.get("text", "") or r.get("content_preview", "")

            meta = dict(chunk_ref.get("metadata", {}))
            meta.update(r.get("metadata", {}))
            meta["chunk_id"] = cid
            meta["model_name"] = r.get("model_name", "Qwen/Qwen3-Embedding-0.6B")
            meta["embedding_dimension"] = coll_qwen_dim
            meta["modality"] = "text"

            b_ids.append(cid)
            b_vecs.append(vec)
            b_docs.append(doc_text)
            b_metas.append(sanitize_metadata(meta))

        coll_qwen.upsert(
            ids=b_ids,
            embeddings=b_vecs,
            documents=b_docs,
            metadatas=b_metas
        )
        if (b_idx + 1) % 5 == 0 or (b_idx + 1) == total_qwen_batches:
            print(f"    - Batch {b_idx + 1:2d}/{total_qwen_batches:2d} hoàn tất ({min((b_idx+1)*batch_size, len(qwen_records)):,}/{len(qwen_records):,} chunks)")

    qwen_duration = time.time() - qwen_start_time
    qwen_count = coll_qwen.count()
    print(f"  ✅ Hoàn thành qwen3_text: {qwen_count:,}/{coll_qwen_expected:,} chunks trong {qwen_duration:.2f}s (~{len(qwen_records)/max(qwen_duration,0.001):.1f} chunks/s)")

    # =========================================================================
    # 5. INGESTION COLLECTION 2: jina_code (937 chunks, 768-dim, cosine)
    # =========================================================================
    print("\n" + "-" * 70)
    print("📦 INGESTION COLLECTION 2: jina_code (768-dim, Cosine HNSW)")
    print("-" * 70)
    coll_jina_name = "jina_code"
    coll_jina_dim = 768
    coll_jina_expected = 937

    coll_jina = client.get_or_create_collection(
        name=coll_jina_name,
        metadata={"hnsw:space": "cosine", "description": "jina-embeddings-v2-base-code 768-dim code collection"}
    )
    print(f"  • Collection '{coll_jina_name}' đã sẵn sàng.")

    jina_records = []
    with open(jina_vector_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                jina_records.append(json.loads(line))
    print(f"  • Đã đọc {len(jina_records):,} records từ vector Jina Code.")
    assert len(jina_records) == coll_jina_expected, f"Kỳ vọng {coll_jina_expected}, có {len(jina_records)}"

    total_jina_batches = math.ceil(len(jina_records) / batch_size)
    jina_start_time = time.time()

    for b_idx in range(total_jina_batches):
        batch = jina_records[b_idx * batch_size : (b_idx + 1) * batch_size]
        b_ids, b_vecs, b_docs, b_metas = [], [], [], []

        for r in batch:
            cid = r["chunk_id"]
            vec = r["vector"]
            assert len(vec) == coll_jina_dim, f"Sai dim Jina tại chunk {cid}: {len(vec)}"

            chunk_ref = chunks_map.get(cid, {})
            doc_text = chunk_ref.get("text", "") or r.get("content_preview", "")

            meta = dict(chunk_ref.get("metadata", {}))
            meta.update(r.get("metadata", {}))
            meta["chunk_id"] = cid
            meta["model_name"] = r.get("model_name", "jinaai/jina-embeddings-v2-base-code")
            meta["embedding_dimension"] = coll_jina_dim
            meta["modality"] = "code"

            b_ids.append(cid)
            b_vecs.append(vec)
            b_docs.append(doc_text)
            b_metas.append(sanitize_metadata(meta))

        coll_jina.upsert(
            ids=b_ids,
            embeddings=b_vecs,
            documents=b_docs,
            metadatas=b_metas
        )
        print(f"    - Batch {b_idx + 1:2d}/{total_jina_batches:2d} hoàn tất ({min((b_idx+1)*batch_size, len(jina_records)):,}/{len(jina_records):,} chunks)")

    jina_duration = time.time() - jina_start_time
    jina_count = coll_jina.count()
    print(f"  ✅ Hoàn thành jina_code: {jina_count:,}/{coll_jina_expected:,} chunks trong {jina_duration:.2f}s (~{len(jina_records)/max(jina_duration,0.001):.1f} chunks/s)")

    # =========================================================================
    # 6. KIỂM THỬ LƯU TRỮ VĨNH VIỄN (COLD RESTART PERSISTENCE & FLUSH TO DISK)
    # =========================================================================
    print("\n" + "=" * 70)
    print("🔄 KIỂM THỬ LƯU TRỮ VĨNH VIỄN (COLD RESTART PERSISTENCE)")
    print("-" * 70)
    del coll_qwen, coll_jina, client
    gc.collect()

    fresh_client = chromadb.PersistentClient(path=str(db_path))
    coll_qwen = fresh_client.get_collection("qwen3_text")
    coll_jina = fresh_client.get_collection("jina_code")

    persisted_qwen_count = coll_qwen.count()
    persisted_jina_count = coll_jina.count()

    print(f"  • Số lượng qwen3_text sau khi nạp: {persisted_qwen_count:,} (Kỳ vọng: 4,293)")
    print(f"  • Số lượng jina_code sau khi nạp : {persisted_jina_count:,} (Kỳ vọng: 937)")
    assert persisted_qwen_count == 4293, f"Sai count qwen3_text: {persisted_qwen_count}"
    assert persisted_jina_count == 937, f"Sai count jina_code: {persisted_jina_count}"
    print("  ✅ Xác thực Cold Restart thành công: 4,293 Text + 937 Code = 5,230 chunks nguyên vẹn!")

    # =========================================================================
    # 7. KIỂM THỬ TRUY VẤN MẪU (NEAREST NEIGHBOR VERIFICATION)
    # =========================================================================
    print("\n" + "=" * 70)
    print("🔍 KIỂM THỬ TRUY VẤN MẪU (NEAREST-NEIGHBOR QUERY TEST)")
    print("-" * 70)

    # Test Qwen text query (dùng vector mẫu đầu tiên)
    sample_text_vec = qwen_records[0]["vector"]
    t0 = time.time()
    test_res_qwen = coll_qwen.query(
        query_embeddings=[sample_text_vec],
        n_results=3,
        include=["documents", "metadatas", "distances"]
    )
    t_qwen = (time.time() - t0) * 1000
    print(f"  • Truy vấn thử nghiệm Qwen3 Text (Thời gian: {t_qwen:.2f}ms):")
    for idx in range(len(test_res_qwen["ids"][0])):
        cid = test_res_qwen["ids"][0][idx]
        dist = test_res_qwen["distances"][0][idx]
        title = test_res_qwen["metadatas"][0][idx].get("section_title", "")
        print(f"    [{idx+1}] ID: {cid} | Cosine Dist: {dist:.4f} | Tiêu đề: {title}")

    # Test Jina code query (dùng vector mẫu đầu tiên)
    sample_code_vec = jina_records[0]["vector"]
    t0 = time.time()
    test_res_jina = coll_jina.query(
        query_embeddings=[sample_code_vec],
        n_results=3,
        include=["documents", "metadatas", "distances"]
    )
    t_jina = (time.time() - t0) * 1000
    print(f"\n  • Truy vấn thử nghiệm Jina Code (Thời gian: {t_jina:.2f}ms):")
    for idx in range(len(test_res_jina["ids"][0])):
        cid = test_res_jina["ids"][0][idx]
        dist = test_res_jina["distances"][0][idx]
        title = test_res_jina["metadatas"][0][idx].get("section_title", "")
        print(f"    [{idx+1}] ID: {cid} | Cosine Dist: {dist:.4f} | Tiêu đề: {title}")

    total_time = time.time() - start_total_time
    print("\n" + "=" * 70)
    print(f"🎉 NẠP VECTOR VÀO CHROMADB THÀNH CÔNG 100% TRONG {total_time:.2f} GIÂY!")
    print("=" * 70)

if __name__ == "__main__":
    main()
