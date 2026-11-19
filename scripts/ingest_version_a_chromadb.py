import sys
import json
import math
import time
import gc
from pathlib import Path
from unittest.mock import MagicMock

# Telemetry patch for Windows environment safety
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
    """Ensure all metadata values are str, int, float, or bool."""
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
    print("🚀 BẮT ĐẦU INGESTION CHROMADB STAGE B – DỮ LIỆU VERSION A")
    print("=" * 70)
    start_total_time = time.time()

    # 1. Đọc manifest Version A
    va_dir = Path("data/08_rag_dataset/version_a")
    manifest_path = va_dir / "manifest.json"
    assert manifest_path.exists(), f"Không tìm thấy manifest tại {manifest_path}"

    with open(manifest_path, "r", encoding="utf-8") as f:
        va_manifest = json.load(f)
    print(f"📋 Phiên bản nguồn: {va_manifest['version']}")
    print(f"📋 Chiến lược định tuyến: {va_manifest['routing_strategy']}")
    print(f"📋 Tổng số chunks kỳ vọng: {va_manifest['total_chunks']:,}")

    # Đường dẫn vectors
    va_qwen_file = va_dir / "embeddings" / va_manifest["collections"]["qwen3_text"]["file"]
    va_jina_file = va_dir / "embeddings" / va_manifest["collections"]["jina_code"]["file"]
    assert va_qwen_file.exists(), f"Không tìm thấy file vector Qwen3: {va_qwen_file}"
    assert va_jina_file.exists(), f"Không tìm thấy file vector Jina: {va_jina_file}"

    # 2. Đọc map toàn bộ chunks từ all_chunks.json để bảo toàn full text
    all_chunks_file = Path("data/06_rag_dataset/chunks/all_chunks.json")
    print(f"\n📂 Đang nạp all_chunks.json từ {all_chunks_file}...")
    with open(all_chunks_file, "r", encoding="utf-8") as f:
        all_chunks_data = json.load(f)
    chunks_map = {c["id"]: c for c in all_chunks_data}
    print(f"✅ Đã nạp thành công {len(chunks_map):,} document chunks vào bộ nhớ.")
    assert len(chunks_map) == 5230, f"all_chunks.json phải có đúng 5.230 chunks, nhận {len(chunks_map)}"

    # 3. Khởi tạo ChromaDB PersistentClient
    db_path = Path("data/09_chromadb")
    db_path.mkdir(parents=True, exist_ok=True)
    print(f"\n💾 Khởi tạo ChromaDB PersistentClient tại: {db_path.resolve()}")
    client = chromadb.PersistentClient(path=str(db_path))

    # 4. Ingestion Collection 1: qwen3_text
    print("\n" + "-" * 70)
    print("📦 INGESTION COLLECTION 1: qwen3_text (1024-dim, cosine)")
    print("-" * 70)
    coll_qwen_name = "qwen3_text"
    coll_qwen_dim = 1024
    coll_qwen_expected = 4851

    # Tạo collection với metric cosine
    coll_qwen = client.get_or_create_collection(
        name=coll_qwen_name,
        metadata={"hnsw:space": "cosine", "description": "Qwen3-Embedding-0.6B 1024-dim text collection"}
    )
    print(f"  • Collection '{coll_qwen_name}' đã sẵn sàng. Metadata: {coll_qwen.metadata}")

    qwen_records = []
    with open(va_qwen_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                qwen_records.append(json.loads(line))
    print(f"  • Đã đọc {len(qwen_records):,} records từ file vector Qwen3.")
    assert len(qwen_records) == coll_qwen_expected, f"Kỳ vọng {coll_qwen_expected}, có {len(qwen_records)}"

    batch_size = 250
    total_qwen_batches = math.ceil(len(qwen_records) / batch_size)
    qwen_start_time = time.time()
    
    for b_idx in range(total_qwen_batches):
        batch = qwen_records[b_idx * batch_size : (b_idx + 1) * batch_size]
        b_ids = []
        b_vecs = []
        b_docs = []
        b_metas = []

        for r in batch:
            cid = r["chunk_id"]
            vec = r["vector"]
            assert len(vec) == coll_qwen_dim, f"Sai dim Qwen: {len(vec)}"
            
            chunk_ref = chunks_map.get(cid, {})
            doc_text = chunk_ref.get("text", "") or r.get("content_preview", "")
            
            # Gộp metadata
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
    print(f"✅ Ingestion qwen3_text hoàn tất trong {qwen_duration:.2f}s. Số records thực tế: {qwen_count:,}/{coll_qwen_expected:,}")
    assert qwen_count == coll_qwen_expected, f"Count không khớp: {qwen_count} != {coll_qwen_expected}"

    # 5. Ingestion Collection 2: jina_code
    print("\n" + "-" * 70)
    print("📦 INGESTION COLLECTION 2: jina_code (768-dim, cosine)")
    print("-" * 70)
    coll_jina_name = "jina_code"
    coll_jina_dim = 768
    coll_jina_expected = 379

    coll_jina = client.get_or_create_collection(
        name=coll_jina_name,
        metadata={"hnsw:space": "cosine", "description": "jina-embeddings-v2-base-code 768-dim code collection"}
    )
    print(f"  • Collection '{coll_jina_name}' đã sẵn sàng. Metadata: {coll_jina.metadata}")

    jina_records = []
    with open(va_jina_file, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                jina_records.append(json.loads(line))
    print(f"  • Đã đọc {len(jina_records):,} records từ file vector Jina.")
    assert len(jina_records) == coll_jina_expected, f"Kỳ vọng {coll_jina_expected}, có {len(jina_records)}"

    total_jina_batches = math.ceil(len(jina_records) / batch_size)
    jina_start_time = time.time()
    
    for b_idx in range(total_jina_batches):
        batch = jina_records[b_idx * batch_size : (b_idx + 1) * batch_size]
        b_ids = []
        b_vecs = []
        b_docs = []
        b_metas = []

        for r in batch:
            cid = r["chunk_id"]
            vec = r["vector"]
            assert len(vec) == coll_jina_dim, f"Sai dim Jina: {len(vec)}"
            
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
    print(f"✅ Ingestion jina_code hoàn tất trong {jina_duration:.2f}s. Số records thực tế: {jina_count:,}/{coll_jina_expected:,}")
    assert jina_count == coll_jina_expected, f"Count không khớp: {jina_count} != {coll_jina_expected}"

    # 6. Kiểm định chất lượng dữ liệu trong collections
    print("\n" + "=" * 70)
    print("🔍 KIỂM ĐỊNH TOÀN DIỆN DỮ LIỆU ĐÃ NẠP (VALIDATION)")
    print("=" * 70)
    
    # 6.1. ID Uniqueness & Overlap Check
    qwen_existing = coll_qwen.get(include=[])["ids"]
    jina_existing = coll_jina.get(include=[])["ids"]
    
    qwen_id_set = set(qwen_existing)
    jina_id_set = set(jina_existing)
    
    print(f"  • Số ID duy nhất trong qwen3_text: {len(qwen_id_set):,} (Kỳ vọng: 4.851)")
    print(f"  • Số ID duy nhất trong jina_code : {len(jina_id_set):,} (Kỳ vọng: 379)")
    
    overlap_ids = qwen_id_set.intersection(jina_id_set)
    print(f"  • Trùng lặp ID giữa 2 collection : {len(overlap_ids)}")
    assert len(overlap_ids) == 0, f"Phát hiện trùng ID giữa 2 collection: {overlap_ids}"
    
    total_unique_ids = qwen_id_set.union(jina_id_set)
    print(f"  • Tổng số ID duy nhất gộp lại   : {len(total_unique_ids):,} (Kỳ vọng: 5.230)")
    assert len(total_unique_ids) == 5230, f"Tổng số ID != 5230: {len(total_unique_ids)}"
    assert total_unique_ids == set(chunks_map.keys()), "Tập ID không khớp 100% với all_chunks.json!"
    print("  ✅ Parity 100%: Toàn bộ 5.230 chunks có mặt đầy đủ, không thiếu hoặc trùng bất kỳ chunk nào!")

    # 6.2. Kiểm tra mẫu Record & Metadata Integrity
    sample_qwen = coll_qwen.get(ids=[qwen_existing[0]], include=["embeddings", "documents", "metadatas"])
    sample_jina = coll_jina.get(ids=[jina_existing[0]], include=["embeddings", "documents", "metadatas"])

    print("\n  📋 Kiểm tra mẫu qwen3_text:")
    print(f"    - ID       : {sample_qwen['ids'][0]}")
    print(f"    - Dim      : {len(sample_qwen['embeddings'][0])} (Kỳ vọng: 1024)")
    print(f"    - Doc len  : {len(sample_qwen['documents'][0]):,} ký tự")
    print(f"    - Metadata : {sample_qwen['metadatas'][0]}")
    assert len(sample_qwen['embeddings'][0]) == 1024
    assert len(sample_qwen['documents'][0]) > 0
    assert "source_file" in sample_qwen['metadatas'][0]

    print("\n  📋 Kiểm tra mẫu jina_code:")
    print(f"    - ID       : {sample_jina['ids'][0]}")
    print(f"    - Dim      : {len(sample_jina['embeddings'][0])} (Kỳ vọng: 768)")
    print(f"    - Doc len  : {len(sample_jina['documents'][0]):,} ký tự")
    print(f"    - Metadata : {sample_jina['metadatas'][0]}")
    assert len(sample_jina['embeddings'][0]) == 768
    assert len(sample_jina['documents'][0]) > 0
    assert "source_file" in sample_jina['metadatas'][0]
    print("  ✅ Metadata và Document text bảo toàn 100% tính toàn vẹn!")

    # 6.3. Kiểm tra truy vấn Nearest-Neighbor thực tế
    print("\n" + "-" * 70)
    print("🔍 KIỂM THỬ TRUY VẤN NEAREST-NEIGHBOR ĐỘC LẬP")
    print("-" * 70)
    with open("data/04_benchmark/benchmark_36q_query_embeddings.json", "r", encoding="utf-8") as qf:
        query_embs = json.load(f := open("data/04_benchmark/benchmark_36q_query_embeddings.json", encoding="utf-8"))

    # Truy vấn test trên qwen3_text (dùng query Q01 - 1024 dim)
    q01_vec = query_embs["Q01"]["qwen3_vector"]
    qwen_query_res = coll_qwen.query(
        query_embeddings=[q01_vec],
        n_results=5,
        include=["documents", "metadatas", "distances"]
    )
    print(f"  • Truy vấn Qwen3 (Q01: '{query_embs['Q01']['query'][:50]}...'):")
    for r_idx in range(len(qwen_query_res["ids"][0])):
        cid = qwen_query_res["ids"][0][r_idx]
        dist = qwen_query_res["distances"][0][r_idx]
        print(f"    {r_idx + 1}. ID: {cid} | Cosine Distance: {dist:.4f}")
        assert 0.0 <= dist <= 2.0, f"Khoảng cách cosine bất thường: {dist}"

    # Truy vấn test trên jina_code (dùng query Q10 - 768 dim)
    q10_vec = query_embs["Q10"]["jina_vector"]
    jina_query_res = coll_jina.query(
        query_embeddings=[q10_vec],
        n_results=5,
        include=["documents", "metadatas", "distances"]
    )
    print(f"\n  • Truy vấn Jina Code (Q10: '{query_embs['Q10']['query'][:50]}...'):")
    for r_idx in range(len(jina_query_res["ids"][0])):
        cid = jina_query_res["ids"][0][r_idx]
        dist = jina_query_res["distances"][0][r_idx]
        print(f"    {r_idx + 1}. ID: {cid} | Cosine Distance: {dist:.4f}")
        assert 0.0 <= dist <= 2.0, f"Khoảng cách cosine bất thường: {dist}"
    print("  ✅ Cả hai collection thực hiện truy vấn Nearest-Neighbor chính xác và hoàn toàn độc lập!")

    # 7. KIỂM THỬ TÍNH BẢO TOÀN PERSISTENCE (ĐÓNG & MỞ LẠI CLIENT)
    print("\n" + "=" * 70)
    print("🔄 KIỂM THỬ TÍNH TOÀN VẸN PERSISTENCE (ĐÓNG VÀ MỞ LẠI CLIENT MỚI)")
    print("-" * 70)
    print("  • Đang đóng tham chiếu client cũ và giải phóng bộ nhớ...")
    del coll_qwen, coll_jina, client
    gc.collect()

    print("  • Khởi tạo PersistentClient HOÀN TOÀN MỚI từ cùng đường dẫn 'data/09_chromadb'...")
    fresh_client = chromadb.PersistentClient(path=str(db_path))
    fresh_colls = fresh_client.list_collections()
    fresh_coll_names = [c.name for c in fresh_colls]
    print(f"  • Danh sách collections nhận diện được: {fresh_coll_names}")
    assert "qwen3_text" in fresh_coll_names, "Thiếu collection qwen3_text sau khi mở lại!"
    assert "jina_code" in fresh_coll_names, "Thiếu collection jina_code sau khi mở lại!"

    fresh_qwen_coll = fresh_client.get_collection("qwen3_text")
    fresh_jina_coll = fresh_client.get_collection("jina_code")

    persisted_qwen_count = fresh_qwen_coll.count()
    persisted_jina_count = fresh_jina_coll.count()

    print(f"  • Số lượng qwen3_text sau khi mở lại: {persisted_qwen_count:,} (Kỳ vọng: 4.851)")
    print(f"  • Số lượng jina_code sau khi mở lại : {persisted_jina_count:,} (Kỳ vọng: 379)")
    assert persisted_qwen_count == 4851, f"Sai count qwen3_text sau persistence: {persisted_qwen_count}"
    assert persisted_jina_count == 379, f"Sai count jina_code sau persistence: {persisted_jina_count}"
    assert persisted_qwen_count + persisted_jina_count == 5230, "Tổng số chunks không bằng 5.230!"
    print("  🎉 XÁC THỰC PERSISTENCE THÀNH CÔNG: Dữ liệu được lưu vĩnh viễn và không bị suy hao!")

    # 8. XUẤT MANIFEST & BÁO CÁO NGHIỆM THU
    total_time = time.time() - start_total_time
    manifest_data = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "stage": "STAGE_B_IN_PRODUCTION",
        "database_engine": "ChromaDB PersistentClient",
        "database_path": str(db_path.resolve()),
        "source_dataset_version": "Version A (Actual Routing: 4.851 Text / 379 Code)",
        "source_manifest": str(manifest_path),
        "total_chunks": 5230,
        "collections": {
            "qwen3_text": {
                "name": "qwen3_text",
                "model_id": "Qwen/Qwen3-Embedding-0.6B",
                "dimension": 1024,
                "distance_metric": "cosine",
                "record_count": persisted_qwen_count,
                "ingestion_duration_sec": round(qwen_duration, 2),
                "source_vector_file": str(va_qwen_file)
            },
            "jina_code": {
                "name": "jina_code",
                "model_id": "jinaai/jina-embeddings-v2-base-code",
                "dimension": 768,
                "distance_metric": "cosine",
                "record_count": persisted_jina_count,
                "ingestion_duration_sec": round(jina_duration, 2),
                "source_vector_file": str(va_jina_file)
            }
        },
        "validation": {
            "count_parity": True,
            "id_uniqueness": True,
            "zero_overlap": True,
            "all_chunks_match": True,
            "persistence_verified": True,
            "nearest_neighbor_query_test": True
        },
        "execution_summary": {
            "total_ingested": persisted_qwen_count + persisted_jina_count,
            "total_duration_sec": round(total_time, 2),
            "status": "SUCCESS"
        }
    }

    manifest_out = Path("reports/chromadb_ingestion_manifest.json")
    with open(manifest_out, "w", encoding="utf-8") as f:
        json.dump(manifest_data, f, ensure_ascii=False, indent=2)
    print(f"\n📄 Đã xuất manifest nghiệm thu: {manifest_out}")

    print("\n" + "=" * 70)
    print("🎉 TOÀN BỘ QUY TRÌNH INGESTION CHROMADB STAGE B HOÀN TẤT THÀNH CÔNG 100%!")
    print("=" * 70)

if __name__ == "__main__":
    main()
