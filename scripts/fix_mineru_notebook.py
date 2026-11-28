# -*- coding: utf-8 -*-
"""
Restore mineru.ipynb from template and apply strict memory patch.
Verify that all code cells in mineru.ipynb compile without syntax errors.
"""
import json
import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = BASE_DIR / "notebooks" / "MinerU_Kaggle_2GPU_DocumentFolders_Resume.ipynb"
DEST_PATH = BASE_DIR / "scratch" / "kaggle_mineru" / "mineru.ipynb"

def main():
    print("=" * 60)
    print("🔧 REPAIRING & VALIDATING MINERU.IPYNB")
    print("=" * 60)

    nb = json.loads(TEMPLATE_PATH.read_text(encoding="utf-8"))

    # Apply memory patch to cell 6
    cell_6_src = "".join(nb["cells"][6]["source"])
    
    # Target in WORKER_CODE:
    # "if work_dir.exists():\n        shutil.rmtree(work_dir)\n\n    return info"
    # Escaped inside single quote string as:
    # "if work_dir.exists():\\n        shutil.rmtree(work_dir)\\n\\n    return info"
    
    target = "if work_dir.exists():\\n        shutil.rmtree(work_dir)\\n\\n    return info"
    replacement = (
        "if work_dir.exists():\\n        shutil.rmtree(work_dir)\\n\\n"
        "    del result\\n"
        "    del middle_data\\n"
        "    del md\\n"
        "    gc.collect()\\n"
        "    try:\\n"
        "        import torch\\n"
        "        if torch.cuda.is_available():\\n"
        "            torch.cuda.empty_cache()\\n"
        "    except Exception:\\n"
        "        pass\\n\\n"
        "    return info"
    )

    if target in cell_6_src:
        cell_6_src = cell_6_src.replace(target, replacement)
        nb["cells"][6]["source"] = [cell_6_src]
        print("✅ Applied memory cleanup patch to process_job()")
    else:
        print("⚠️ Target pattern not found in cell 6!")

    # Verify all code cells
    has_error = False
    for i, cell in enumerate(nb["cells"]):
        if cell.get("cell_type") == "code":
            src = "".join(cell.get("source", []))
            try:
                compile(src, f"cell_{i}", "exec")
                print(f"  • Cell {i:02d} ({len(src):5d} chars): COMPILED OK")
            except SyntaxError as e:
                print(f"❌ Cell {i:02d} SYNTAX ERROR: {e}")
                has_error = True

    if has_error:
        raise RuntimeError("One or more code cells failed compilation!")

    DEST_PATH.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"✅ Successfully written verified notebook to: {DEST_PATH}")

if __name__ == "__main__":
    main()
