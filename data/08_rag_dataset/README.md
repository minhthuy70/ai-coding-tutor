# 08_rag_dataset — Thư mục lưu trữ Vectors & Checkpoints Embedding

Thư mục này là đích đến chuẩn của toàn bộ dữ liệu Embedding sinh ra từ Kaggle Cloud GPU:

## Cấu trúc thư mục:

```
08_rag_dataset/
├── embeddings/
│   ├── qwen3_text/
│   │   └── qwen3_text_vectors.jsonl        # 4.293 vectors (1024-dim, Last-Token Pooling)
│   └── jina_code/
│       └── jina_code_vectors.jsonl          # 937 vectors (768-dim, Attention-Masked Mean)
├── reports/
│   └── kaggle_embedding_benchmark_report.json # Báo cáo đo đạc VRAM, thời gian và số lượng vector
└── checkpoints/
    ├── qwen3_text/                          # Checkpoint batches của Qwen3
    └── jina_code/                           # Checkpoint batches của Jina Code
```

Khi tải file `ai_coding_tutor_embeddings_bundle.tar.gz` từ Kaggle về, bạn có thể thả file trực tiếp vào đây hoặc thư mục gốc dự án để giải nén.
