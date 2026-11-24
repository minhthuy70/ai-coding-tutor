import os
import sys
import json
import math
import tarfile
from pathlib import Path

def validate_delta_bundle(bundle_path: Path, expected_chunks_path: Path):
    print("=" * 70)
    print("🔍 KIỂM TOÁN ĐỘC LẬP GÓI ARTIFACT DELTA JINA EMBEDDINGS (558 CHUNKS)")
    print("=" * 70)
    print(f"📦 Đường dẫn bundle: {bundle_path} ({bundle_path.stat().st_size:,} bytes)")
    
    # 1. Mở archive tar.gz
    assert bundle_path.exists(), f"Không tìm thấy file bundle tại {bundle_path}"
    with tarfile.open(bundle_path, "r:gz") as tar:
        members = tar.getnames()
        print(f"📂 Danh sách thành phần trong archive ({len(members)} entries):")
        for m in sorted(members):
            print(f"  • {m}")
            
        # Trích xuất vào thư mục tạm hoặc kiểm tra in-memory
        extract_dir = bundle_path.parent / "extracted_delta_558"
        extract_dir.mkdir(parents=True, exist_ok=True)
        tar.extractall(extract_dir)

    # 2. Đọc file chunks đầu vào để đối soát IDs
    with open(expected_chunks_path, "r", encoding="utf-8") as f:
        expected_chunks = json.load(f)
    expected_ids = {c["id"]: c for c in expected_chunks}
    print(f"\n📋 Số lượng chunks kỳ vọng: {len(expected_ids):,}")

    # 3. Đọc và kiểm định file vectors jina_code
    vectors_file = extract_dir / "embeddings" / "jina_code" / "jina_code_vectors.jsonl"
    assert vectors_file.exists(), f"Không tìm thấy file vectors tại {vectors_file}"

    seen_ids = set()
    records = []
    dim_target = 768
    l2_tolerance = 5e-3
    nan_inf_count = 0
    l2_norm_errors = 0
    dim_errors = 0
    model_name_errors = 0
    
    with open(vectors_file, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            if not line.strip():
                continue
            rec = json.loads(line)
            cid = rec.get("chunk_id")
            seen_ids.add(cid)
            records.append(rec)
            
            # Kiểm tra model
            if rec.get("model_name") != "jinaai/jina-embeddings-v2-base-code":
                model_name_errors += 1
                
            vec = rec.get("vector", [])
            # Kiểm tra dim
            if len(vec) != dim_target:
                dim_errors += 1
                
            # Kiểm tra NaN/Inf & L2
            l2_sum = 0.0
            has_nan_inf = False
            for v in vec:
                if math.isnan(v) or math.isinf(v):
                    has_nan_inf = True
                    break
                l2_sum += v * v
            if has_nan_inf:
                nan_inf_count += 1
            else:
                l2_norm = math.sqrt(l2_sum)
                if abs(l2_norm - 1.0) > l2_tolerance:
                    l2_norm_errors += 1

    print("\n📊 KẾT QUẢ KIỂM ĐỊNH CHI TIẾT:")
    print(f"  • Tổng số vector đọc được : {len(records):,}")
    print(f"  • Số ID duy nhất          : {len(seen_ids):,}")
    print(f"  • Trùng lặp ID            : {len(records) - len(seen_ids)}")
    print(f"  • Sai lệch Model Identity : {model_name_errors}")
    print(f"  • Sai lệch Dimension (768): {dim_errors}")
    print(f"  • Lỗi NaN / Inf           : {nan_inf_count}")
    print(f"  • Sai lệch L2-Norm (tol)  : {l2_norm_errors}")

    # Đối chiếu ID với expected
    missing_ids = set(expected_ids.keys()) - seen_ids
    unexpected_ids = seen_ids - set(expected_ids.keys())
    print(f"  • Missing IDs             : {len(missing_ids)}")
    print(f"  • Unexpected IDs          : {len(unexpected_ids)}")

    # 4. Kiểm tra benchmark report JSON đi kèm
    report_json_path = extract_dir / "reports" / "kaggle_embedding_benchmark_report.json"
    if report_json_path.exists():
        with open(report_json_path, "r", encoding="utf-8") as rf:
            rep = json.load(rf)
        print(f"\n📋 Báo cáo Kaggle đính kèm:")
        print(f"  • Input file              : {rep.get('input_file')}")
        print(f"  • Qwen3 target / completed: {rep.get('qwen3_text', {}).get('target_chunks')} / {rep.get('qwen3_text', {}).get('completed_vectors')}")
        print(f"  • Jina Code completed     : {rep.get('jina_code', {}).get('completed_vectors')}")
        print(f"  • Jina Pooling Mode       : {rep.get('jina_code', {}).get('pooling_mode')}")
        print(f"  • Jina Inference time     : {rep.get('jina_code', {}).get('inference_time_sec')}s")
        print(f"  • Peak VRAM               : {rep.get('jina_code', {}).get('peak_vram_gb')} GB")

    # Assertions
    assert len(records) == 558, f"Kỳ vọng 558 vector, nhận được {len(records)}"
    assert len(seen_ids) == 558, f"Trùng lặp ID!"
    assert missing_ids == set(), f"Thiếu ID: {missing_ids}"
    assert unexpected_ids == set(), f"Thừa ID: {unexpected_ids}"
    assert dim_errors == 0, f"Có vector sai dimension!"
    assert nan_inf_count == 0, f"Có vector NaN/Inf!"
    assert l2_norm_errors == 0, f"Có vector chưa chuẩn hóa L2!"
    assert model_name_errors == 0, f"Sai model identity!"
    
    print("\n" + "=" * 70)
    print("🎉 TẤT CẢ TIÊU CHÍ VALIDATION: PASS 100%!")
    print("=" * 70)
    return True

if __name__ == "__main__":
    bundle = Path("artifacts/ai_coding_tutor_embeddings_delta_558.tar.gz")
    delta_chunks = Path("data/06_rag_dataset/chunks/ab_test_558_jina_delta.json")
    validate_delta_bundle(bundle, delta_chunks)
