import json
from pathlib import Path

nb_path = Path("notebooks/Kaggle_Embedding_Pipeline_GPU.ipynb")
nb = json.loads(nb_path.read_text(encoding="utf-8"))

for i, cell in enumerate(nb["cells"]):
    print(f"\n{'='*30} CELL {i} ({cell.get('cell_type')}) {'='*30}")
    src = "".join(cell.get("source", []))
    print(src[:800])
    if len(src) > 800:
        print(f"... [truncated, total {len(src)} chars]")
