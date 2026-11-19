import json
import math
from pathlib import Path
from typing import List, Dict, Any, Tuple
import numpy as np

def load_vector_file(path: Path) -> Tuple[List[str], np.ndarray]:
    """Loads JSONL file and returns list of chunk_ids and normalized numpy matrix."""
    ids = []
    vectors = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): continue
            rec = json.loads(line)
            ids.append(rec["chunk_id"])
            vectors.append(rec["vector"])
    mat = np.array(vectors, dtype=np.float32)
    # Ensure L2 normalized
    norms = np.linalg.norm(mat, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    mat = mat / norms
    return ids, mat

def retrieve_top_n(query_vec: np.ndarray, doc_ids: List[str], doc_mat: np.ndarray, top_n: int = 20) -> List[Tuple[str, float, int]]:
    """
    Computes cosine similarity between query and doc_mat, returns top_n (chunk_id, distance, rank).
    Tie-breaking: cosine distance ascending, then chunk_id lexical ascending.
    """
    if len(doc_ids) == 0:
        return []
    
    # Query vector normalization
    q_norm = np.linalg.norm(query_vec)
    if q_norm > 0:
        q_vec = query_vec / q_norm
    else:
        q_vec = query_vec

    sims = np.dot(doc_mat, q_vec)
    dists = 1.0 - sims
    
    # Pack for deterministic sort: (distance, chunk_id, index)
    items = [(float(dists[i]), doc_ids[i]) for i in range(len(doc_ids))]
    # Sort: distance ascending, chunk_id ascending
    items.sort(key=lambda x: (x[0], x[1]))
    
    selected = items[:top_n]
    # Return (chunk_id, distance, 1-based rank)
    return [(cid, dist, rank + 1) for rank, (dist, cid) in enumerate(selected)]

def rrf_fuse(text_top_n: List[Tuple[str, float, int]], code_top_n: List[Tuple[str, float, int]], k0: int = 60, top_k: int = 5) -> List[Dict[str, Any]]:
    """
    Combines text and code candidates using Reciprocal Rank Fusion.
    Score = sum_m 1.0 / (k0 + rank_m).
    Tie-breaking: min cosine distance across collections, then chunk_id lexical.
    """
    scores: Dict[str, float] = {}
    min_dists: Dict[str, float] = {}
    sources: Dict[str, Dict[str, Any]] = {}

    for cid, dist, rank in text_top_n:
        scores[cid] = scores.get(cid, 0.0) + (1.0 / (k0 + rank))
        min_dists[cid] = min(min_dists.get(cid, 999.0), dist)
        if cid not in sources:
            sources[cid] = {}
        sources[cid]["text_rank"] = rank
        sources[cid]["text_dist"] = dist

    for cid, dist, rank in code_top_n:
        scores[cid] = scores.get(cid, 0.0) + (1.0 / (k0 + rank))
        min_dists[cid] = min(min_dists.get(cid, 999.0), dist)
        if cid not in sources:
            sources[cid] = {}
        sources[cid]["code_rank"] = rank
        sources[cid]["code_dist"] = dist

    # Sort candidates
    all_cids = list(scores.keys())
    all_cids.sort(key=lambda cid: (-scores[cid], min_dists[cid], cid))

    results = []
    for rank, cid in enumerate(all_cids[:top_k], start=1):
        results.append({
            "rank": rank,
            "chunk_id": cid,
            "rrf_score": scores[cid],
            "min_distance": min_dists[cid],
            "details": sources[cid]
        })
    return results

def evaluate_retrieval(benchmark_queries: List[Dict[str, Any]], query_embeddings: Dict[str, Any], text_ids: List[str], text_mat: np.ndarray, code_ids: List[str], code_mat: np.ndarray, version_name: str) -> Dict[str, Any]:
    query_eval_results = []
    
    for q_item in benchmark_queries:
        qid = q_item["id"]
        cat = q_item["category"]
        query_text = q_item["query"]
        gt_chunks = set(q_item["ground_truth_chunks"])
        
        q_emb = query_embeddings[qid]
        qwen_vec = np.array(q_emb["qwen3_vector"], dtype=np.float32)
        jina_vec = np.array(q_emb["jina_vector"], dtype=np.float32)

        # Retrieve top 20 candidates from each collection
        text_top20 = retrieve_top_n(qwen_vec, text_ids, text_mat, top_n=20)
        code_top20 = retrieve_top_n(jina_vec, code_ids, code_mat, top_n=20)

        # RRF Fusion
        fused_top5 = rrf_fuse(text_top20, code_top20, k0=60, top_k=5)
        top3_ids = [res["chunk_id"] for res in fused_top5[:3]]
        top5_ids = [res["chunk_id"] for res in fused_top5[:5]]

        hit_at_3 = 1.0 if bool(set(top3_ids) & gt_chunks) else 0.0
        hit_at_5 = 1.0 if bool(set(top5_ids) & gt_chunks) else 0.0
        
        hits_in_top5 = set(top5_ids) & gt_chunks
        recall_at_5 = len(hits_in_top5) / len(gt_chunks) if len(gt_chunks) > 0 else 0.0

        first_hit_rank = None
        for item in fused_top5:
            if item["chunk_id"] in gt_chunks:
                first_hit_rank = item["rank"]
                break
        
        mrr_at_5 = (1.0 / first_hit_rank) if first_hit_rank is not None else 0.0

        query_eval_results.append({
            "id": qid,
            "category": cat,
            "query": query_text,
            "ground_truth": list(gt_chunks),
            "retrieved_top5": fused_top5,
            "hit_at_3": hit_at_3,
            "hit_at_5": hit_at_5,
            "mrr_at_5": mrr_at_5,
            "recall_at_5": recall_at_5,
            "first_hit_rank": first_hit_rank
        })

    # Aggregate by category and overall
    categories = ["theory", "code", "api", "hybrid"]
    cat_summary = {}
    for cat in categories:
        cat_items = [r for r in query_eval_results if r["category"] == cat]
        cat_summary[cat] = {
            "count": len(cat_items),
            "hit_rate_at_3": float(np.mean([r["hit_at_3"] for r in cat_items])),
            "hit_rate_at_5": float(np.mean([r["hit_at_5"] for r in cat_items])),
            "mrr_at_5": float(np.mean([r["mrr_at_5"] for r in cat_items])),
            "recall_at_5": float(np.mean([r["recall_at_5"] for r in cat_items]))
        }

    overall_summary = {
        "version": version_name,
        "total_queries": len(query_eval_results),
        "hit_rate_at_3": float(np.mean([r["hit_at_3"] for r in query_eval_results])),
        "hit_rate_at_5": float(np.mean([r["hit_at_5"] for r in query_eval_results])),
        "mrr_at_5": float(np.mean([r["mrr_at_5"] for r in query_eval_results])),
        "recall_at_5": float(np.mean([r["recall_at_5"] for r in query_eval_results])),
        "category_summary": cat_summary,
        "queries": query_eval_results
    }
    return overall_summary

def main():
    print("=" * 70)
    print("🚀 BẮT ĐẦU CHẠY BENCHMARK RETRIEVAL A/B: VERSION A vs VERSION B")
    print("=" * 70)

    # 1. Nạp benchmark và query embeddings
    bench_file = Path("data/04_benchmark/routing_ab_eval_36q.json")
    query_emb_file = Path("data/04_benchmark/benchmark_36q_query_embeddings.json")

    assert bench_file.exists(), f"Thiếu file benchmark: {bench_file}"
    assert query_emb_file.exists(), f"Thiếu file query embeddings: {query_emb_file}"

    with open(bench_file, "r", encoding="utf-8") as f:
        benchmark_queries = json.load(f)
    with open(query_emb_file, "r", encoding="utf-8") as f:
        query_embeddings = json.load(f)

    print(f"📋 Đã nạp {len(benchmark_queries)} câu hỏi và {len(query_embeddings)} bộ query embeddings.")

    # 2. Nạp dữ liệu Version A
    print("\n📂 Đang nạp vectors Version A (4.851 Qwen3 + 379 Jina)...")
    va_text_path = Path("data/08_rag_dataset/version_a/embeddings/qwen3_text/qwen3_text_vectors.jsonl")
    va_code_path = Path("data/08_rag_dataset/version_a/embeddings/jina_code/jina_code_vectors.jsonl")
    va_text_ids, va_text_mat = load_vector_file(va_text_path)
    va_code_ids, va_code_mat = load_vector_file(va_code_path)
    print(f"  • Version A Text: {len(va_text_ids):,} vectors (Shape: {va_text_mat.shape})")
    print(f"  • Version A Code: {len(va_code_ids):,} vectors (Shape: {va_code_mat.shape})")

    # 3. Nạp dữ liệu Version B
    print("\n📂 Đang nạp vectors Version B (4.293 Qwen3 + 937 Jina)...")
    vb_text_path = Path("data/08_rag_dataset/version_b/embeddings/qwen3_text/qwen3_text_vectors.jsonl")
    vb_code_path = Path("data/08_rag_dataset/version_b/embeddings/jina_code/jina_code_vectors.jsonl")
    vb_text_ids, vb_text_mat = load_vector_file(vb_text_path)
    vb_code_ids, vb_code_mat = load_vector_file(vb_code_path)
    print(f"  • Version B Text: {len(vb_text_ids):,} vectors (Shape: {vb_text_mat.shape})")
    print(f"  • Version B Code: {len(vb_code_ids):,} vectors (Shape: {vb_code_mat.shape})")

    # 4. Chạy đánh giá Version A
    print("\n🔍 Đang đánh giá Version A...")
    results_va = evaluate_retrieval(
        benchmark_queries, query_embeddings,
        va_text_ids, va_text_mat, va_code_ids, va_code_mat,
        version_name="Version A (Actual Routing: 4851 Text / 379 Code)"
    )

    # 5. Chạy đánh giá Version B
    print("\n🔍 Đang đánh giá Version B...")
    results_vb = evaluate_retrieval(
        benchmark_queries, query_embeddings,
        vb_text_ids, vb_text_mat, vb_code_ids, vb_code_mat,
        version_name="Version B (Pedagogical Tag Dominance: 4293 Text / 937 Code)"
    )

    # 6. So sánh chi tiết
    print("\n" + "=" * 70)
    print("📊 BẢNG SO SÁNH TỔNG THỂ (OVERALL A/B BENCHMARK COMPARISON)")
    print("=" * 70)
    print(f"{'Metric':<18} | {'Version A':<15} | {'Version B':<15} | {'Chênh lệch (B - A)':<18}")
    print("-" * 72)
    metrics = [
        ("Hit Rate@3", "hit_rate_at_3"),
        ("Hit Rate@5", "hit_rate_at_5"),
        ("MRR@5", "mrr_at_5"),
        ("Recall@5", "recall_at_5")
    ]
    for m_label, m_key in metrics:
        val_a = results_va[m_key]
        val_b = results_vb[m_key]
        delta = val_b - val_a
        delta_str = f"{delta:+.4f} ({delta*100:+.2f}%)"
        print(f"{m_label:<18} | {val_a:<15.4f} | {val_b:<15.4f} | {delta_str:<18}")

    print("\n" + "=" * 70)
    print("📊 SO SÁNH THEO TỪNG NHÓM NĂNG LỰC (CATEGORY BREAKDOWN)")
    print("=" * 70)
    categories = ["theory", "code", "api", "hybrid"]
    for cat in categories:
        cat_a = results_va["category_summary"][cat]
        cat_b = results_vb["category_summary"][cat]
        print(f"\n🏷️ NHÓM: {cat.upper()} (9 câu hỏi)")
        print(f"  • Hit Rate@3 : A = {cat_a['hit_rate_at_3']:.4f} | B = {cat_b['hit_rate_at_3']:.4f} (Delta: {cat_b['hit_rate_at_3'] - cat_a['hit_rate_at_3']:+.4f})")
        print(f"  • Hit Rate@5 : A = {cat_a['hit_rate_at_5']:.4f} | B = {cat_b['hit_rate_at_5']:.4f} (Delta: {cat_b['hit_rate_at_5'] - cat_a['hit_rate_at_5']:+.4f})")
        print(f"  • MRR@5      : A = {cat_a['mrr_at_5']:.4f} | B = {cat_b['mrr_at_5']:.4f} (Delta: {cat_b['mrr_at_5'] - cat_a['mrr_at_5']:+.4f})")
        print(f"  • Recall@5   : A = {cat_a['recall_at_5']:.4f} | B = {cat_b['recall_at_5']:.4f} (Delta: {cat_b['recall_at_5'] - cat_a['recall_at_5']:+.4f})")

    # Phân loại câu hỏi
    improved_queries = []
    regressed_queries = []
    both_failed_queries = []
    unchanged_queries = []

    for qa, qb in zip(results_va["queries"], results_vb["queries"]):
        qid = qa["id"]
        # Comparison metric priority: MRR then Hit@5
        mrr_diff = qb["mrr_at_5"] - qa["mrr_at_5"]
        hit_diff = qb["hit_at_5"] - qa["hit_at_5"]
        
        if qa["hit_at_5"] == 0 and qb["hit_at_5"] == 0:
            both_failed_queries.append({
                "id": qid,
                "category": qa["category"],
                "query": qa["query"],
                "ground_truth": qa["ground_truth"]
            })
        elif mrr_diff > 0 or hit_diff > 0:
            improved_queries.append({
                "id": qid,
                "category": qa["category"],
                "query": qa["query"],
                "mrr_a": qa["mrr_at_5"],
                "mrr_b": qb["mrr_at_5"],
                "rank_a": qa["first_hit_rank"],
                "rank_b": qb["first_hit_rank"],
                "delta_mrr": mrr_diff
            })
        elif mrr_diff < 0 or hit_diff < 0:
            regressed_queries.append({
                "id": qid,
                "category": qa["category"],
                "query": qa["query"],
                "mrr_a": qa["mrr_at_5"],
                "mrr_b": qb["mrr_at_5"],
                "rank_a": qa["first_hit_rank"],
                "rank_b": qb["first_hit_rank"],
                "delta_mrr": mrr_diff
            })
        else:
            unchanged_queries.append(qid)

    print("\n" + "=" * 70)
    print("🔍 PHÂN LOẠI CÁC CÂU HỎI:")
    print(f"  • Số câu Version B cải thiện (Improved): {len(improved_queries)}")
    for q in improved_queries:
        print(f"    - [{q['id']}] ({q['category']}): Rank {q['rank_a']} -> {q['rank_b']} (MRR: {q['mrr_a']:.2f} -> {q['mrr_b']:.2f}) | {q['query'][:60]}")
    
    print(f"\n  • Số câu Version B suy giảm (Regressed): {len(regressed_queries)}")
    for q in regressed_queries:
        print(f"    - [{q['id']}] ({q['category']}): Rank {q['rank_a']} -> {q['rank_b']} (MRR: {q['mrr_a']:.2f} -> {q['mrr_b']:.2f}) | {q['query'][:60]}")

    print(f"\n  • Số câu cả hai phiên bản đều thất bại (Both Failed): {len(both_failed_queries)}")
    for q in both_failed_queries:
        print(f"    - [{q['id']}] ({q['category']}): {q['query'][:60]}")

    print(f"\n  • Số câu giữ nguyên hiệu năng (Unchanged): {len(unchanged_queries)}")

    # 7. Xuất file JSON kết quả
    full_output = {
        "timestamp": "2026-11-20T01:40:00Z",
        "benchmark_file": str(bench_file),
        "overall_comparison": {
            "version_a": {k: results_va[k] for k in ["hit_rate_at_3", "hit_rate_at_5", "mrr_at_5", "recall_at_5"]},
            "version_b": {k: results_vb[k] for k in ["hit_rate_at_3", "hit_rate_at_5", "mrr_at_5", "recall_at_5"]},
            "deltas": {k: float(results_vb[k] - results_va[k]) for k in ["hit_rate_at_3", "hit_rate_at_5", "mrr_at_5", "recall_at_5"]}
        },
        "category_comparison": {
            cat: {
                "version_a": results_va["category_summary"][cat],
                "version_b": results_vb["category_summary"][cat],
                "deltas": {k: float(results_vb["category_summary"][cat][k] - results_va["category_summary"][cat][k]) for k in ["hit_rate_at_3", "hit_rate_at_5", "mrr_at_5", "recall_at_5"]}
            } for cat in categories
        },
        "improved_queries": improved_queries,
        "regressed_queries": regressed_queries,
        "both_failed_queries": both_failed_queries,
        "version_a_details": results_va,
        "version_b_details": results_vb
    }

    out_json_path = Path("reports/routing_ab_benchmark_results.json")
    with open(out_json_path, "w", encoding="utf-8") as f:
        json.dump(full_output, f, ensure_ascii=False, indent=2)
    print(f"\n💾 Đã lưu kết quả chi tiết vào: {out_json_path}")

if __name__ == "__main__":
    main()
