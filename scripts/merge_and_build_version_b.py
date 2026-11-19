import json
import math
import shutil
from pathlib import Path

def main():
    print("=" * 70)
    print("🚀 TIẾN HÀNH HỢP NHẤT VÀ TẠO DATASET EMBEDDING VERSION B")
    print("=" * 70)

    # 1. Đường dẫn dữ liệu
    all_chunks_path = Path("data/06_rag_dataset/chunks/all_chunks.json")
    delta_chunks_path = Path("data/06_rag_dataset/chunks/ab_test_558_jina_delta.json")
    
    va_dir = Path("data/08_rag_dataset/version_a/embeddings")
    vb_dir = Path("data/08_rag_dataset/version_b/embeddings")
    
    va_dir.mkdir(parents=True, exist_ok=True)
    vb_dir.mkdir(parents=True, exist_ok=True)
    
    orig_qwen = Path("data/08_rag_dataset/embeddings/qwen3_text/qwen3_text_vectors.jsonl")
    orig_jina = Path("data/08_rag_dataset/embeddings/jina_code/jina_code_vectors.jsonl")
    delta_jina = Path("artifacts/extracted_delta_558/embeddings/jina_code/jina_code_vectors.jsonl")

    # 2. Đọc ground truth all_chunks
    with open(all_chunks_path, "r", encoding="utf-8") as f:
        all_chunks = json.load(f)
    all_chunk_ids = {c["id"] for c in all_chunks}
    print(f"📋 Ground Truth Total Chunks: {len(all_chunk_ids):,}")

    # Đọc delta 558 IDs
    with open(delta_chunks_path, "r", encoding="utf-8") as f:
        delta_chunks = json.load(f)
    delta_ids = {c["id"] for c in delta_chunks}
    print(f"📋 Delta Jina IDs: {len(delta_ids):,}")

    # 3. Chuẩn bị Version A (Copy an toàn từ gốc vào version_a/)
    va_qwen_target = va_dir / "qwen3_text" / "qwen3_text_vectors.jsonl"
    va_jina_target = va_dir / "jina_code" / "jina_code_vectors.jsonl"
    va_qwen_target.parent.mkdir(parents=True, exist_ok=True)
    va_jina_target.parent.mkdir(parents=True, exist_ok=True)
    
    shutil.copy(orig_qwen, va_qwen_target)
    shutil.copy(orig_jina, va_jina_target)
    print(f"✅ Đã đóng băng an toàn Version A tại {va_dir}")

    # 4. Tạo Version B
    vb_qwen_target = vb_dir / "qwen3_text" / "qwen3_text_vectors.jsonl"
    vb_jina_target = vb_dir / "jina_code" / "jina_code_vectors.jsonl"
    vb_qwen_target.parent.mkdir(parents=True, exist_ok=True)
    vb_jina_target.parent.mkdir(parents=True, exist_ok=True)

    # 4.1. Version B Qwen3 = Version A Qwen3 trừ đi 558 delta IDs
    vb_qwen_count = 0
    with open(orig_qwen, "r", encoding="utf-8") as src, open(vb_qwen_target, "w", encoding="utf-8") as dst:
        for line in src:
            if not line.strip(): continue
            rec = json.loads(line)
            if rec["chunk_id"] not in delta_ids:
                dst.write(line)
                vb_qwen_count += 1
    print(f"✅ Version B Qwen3 Text Vectors: {vb_qwen_count:,} (Kỳ vọng: 4.293)")
    assert vb_qwen_count == 4293, f"Sai số lượng Qwen3 Version B: {vb_qwen_count}"

    # 4.2. Version B Jina = Version A Jina (379) + Delta Jina (558) = 937
    vb_jina_count = 0
    with open(vb_jina_target, "w", encoding="utf-8") as dst:
        # Ghi 379 vectors Version A
        with open(orig_jina, "r", encoding="utf-8") as src_a:
            for line in src_a:
                if not line.strip(): continue
                dst.write(line)
                vb_jina_count += 1
        print(f"  • Đã nạp từ Version A Jina: {vb_jina_count:,} vectors")
        
        # Ghi tiếp 558 vectors Delta Jina
        delta_added = 0
        with open(delta_jina, "r", encoding="utf-8") as src_d:
            for line in src_d:
                if not line.strip(): continue
                dst.write(line)
                vb_jina_count += 1
                delta_added += 1
        print(f"  • Đã bổ sung từ Delta Jina: {delta_added:,} vectors")
        
    print(f"✅ Version B Jina Code Vectors: {vb_jina_count:,} (Kỳ vọng: 937)")
    assert vb_jina_count == 937, f"Sai số lượng Jina Version B: {vb_jina_count}"

    # 5. Kiểm toán toàn diện Version B (Parity, Dimension, Norm, No NaN)
    print("\n🔍 ĐANG KIỂM TOÁN CHẤT LƯỢNG DATASET VERSION B...")
    vb_qwen_ids = set()
    with open(vb_qwen_target, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): continue
            rec = json.loads(line)
            cid = rec["chunk_id"]
            assert cid not in vb_qwen_ids, f"Trùng ID Qwen Version B: {cid}"
            assert len(rec["vector"]) == 1024, "Sai dimension Qwen (kỳ vọng 1024)"
            vb_qwen_ids.add(cid)

    vb_jina_ids = set()
    with open(vb_jina_target, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): continue
            rec = json.loads(line)
            cid = rec["chunk_id"]
            assert cid not in vb_jina_ids, f"Trùng ID Jina Version B: {cid}"
            assert len(rec["vector"]) == 768, "Sai dimension Jina (kỳ vọng 768)"
            # kiểm tra L2 norm
            vec = rec["vector"]
            l2_norm = math.sqrt(sum(v*v for v in vec))
            assert abs(l2_norm - 1.0) < 5e-3, f"L2 norm ngoài dung sai: {l2_norm}"
            vb_jina_ids.add(cid)

    overlap = vb_qwen_ids.intersection(vb_jina_ids)
    assert len(overlap) == 0, f"Phát hiện overlap ID giữa Qwen và Jina trong Version B: {overlap}"
    
    vb_total_ids = vb_qwen_ids.union(vb_jina_ids)
    assert len(vb_total_ids) == 5230, f"Tổng số ID Version B không bằng 5230: {len(vb_total_ids)}"
    assert vb_total_ids == all_chunk_ids, "Tập ID Version B không khớp 100% với all_chunks.json!"

    print("🎉 KIỂM TOÁN HOÀN TẤT: Version B đạt chuẩn 100%!")
    print(f"  • Qwen3 Text Vectors : {len(vb_qwen_ids):,}")
    print(f"  • Jina Code Vectors  : {len(vb_jina_ids):,}")
    print(f"  • Tổng số Vectors    : {len(vb_total_ids):,}")
    print(f"  • Khớp all_chunks    : 100% (5.230/5.230)")

    # 6. Ghi manifest JSON cho cả hai phiên bản
    manifest_va = {
        "version": "Version A (Actual Routing)",
        "routing_strategy": "Content-Type & Code Ratio Threshold = 0.50 (Initial)",
        "total_chunks": 5230,
        "collections": {
            "qwen3_text": {
                "model": "Qwen/Qwen3-Embedding-0.6B",
                "dimension": 1024,
                "count": 4851,
                "file": "qwen3_text/qwen3_text_vectors.jsonl"
            },
            "jina_code": {
                "model": "jinaai/jina-embeddings-v2-base-code",
                "dimension": 768,
                "count": 379,
                "file": "jina_code/jina_code_vectors.jsonl"
            }
        }
    }
    with open(Path("data/08_rag_dataset/version_a/manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest_va, f, indent=2)

    manifest_vb = {
        "version": "Version B (Pedagogical Tag Dominance)",
        "routing_strategy": "Pedagogical Tag code_example Dominance + Code Ratio >= 0.50",
        "total_chunks": 5230,
        "collections": {
            "qwen3_text": {
                "model": "Qwen/Qwen3-Embedding-0.6B",
                "dimension": 1024,
                "count": 4293,
                "file": "qwen3_text/qwen3_text_vectors.jsonl"
            },
            "jina_code": {
                "model": "jinaai/jina-embeddings-v2-base-code",
                "dimension": 768,
                "count": 937,
                "file": "jina_code/jina_code_vectors.jsonl"
            }
        },
        "delta_info": {
            "source_bundle": "artifacts/ai_coding_tutor_embeddings_delta_558.tar.gz",
            "delta_chunks_reassigned": 558,
            "reassigned_from": "qwen3_text",
            "reassigned_to": "jina_code"
        }
    }
    with open(Path("data/08_rag_dataset/version_b/manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest_vb, f, indent=2)

    print("📄 Đã tạo manifest cho Version A và Version B thành công!")

if __name__ == "__main__":
    main()
