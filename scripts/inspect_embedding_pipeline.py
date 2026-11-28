import json
from pathlib import Path

nb_path = Path("notebooks/Kaggle_Embedding_Pipeline_GPU.ipynb")
if nb_path.exists():
    nb = json.loads(nb_path.read_text(encoding="utf-8"))
    print("Total cells in Kaggle_Embedding_Pipeline_GPU.ipynb:", len(nb["cells"]))
    for i, cell in enumerate(nb["cells"]):
        src = "".join(cell.get("source", []))
        fl = src.split("\n")[0] if src else ""
        print(f"Cell {i:02d} ({cell.get('cell_type')}): {fl[:80]}")

print("\n" + "="*70)
# Check git history for Kaggle_Embedding_Pipeline_GPU.ipynb or related scripts
report_path = Path("data/08_rag_dataset/reports/kaggle_embedding_benchmark_report.json")
if report_path.exists():
    print("Found kaggle_embedding_benchmark_report.json:")
    print(report_path.read_text(encoding="utf-8")[:1000])
