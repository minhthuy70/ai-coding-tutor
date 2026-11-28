# -*- coding: utf-8 -*-
"""
End-to-End Automated Pipeline for EN_PDF_191 and Final Kaggle GPU Embedding:
1. Monitors minhthuy70/mineru-191-parser until COMPLETE.
2. Downloads and unpacks mineru_rag_output.zip for EN_PDF_191.
3. Runs Markdown Cleaning & QA Validation.
4. Runs AST-Aware Chunking Engine & Deep Audit.
5. Updates Kaggle dataset minhthuy70/embedding with 100% full chunks.
6. Launches Kaggle GPU Dual-Model Embedding Kernel (ai-coding-tutor-embedding-v2).
"""
import time
import sys
import os
import shutil
import zipfile
import subprocess
from datetime import datetime
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

BASE_DIR = Path(__file__).resolve().parent.parent
KERNEL_TARGET = "minhthuy70/mineru-191-parser"
OUTPUT_DIR = BASE_DIR / "scratch" / "kaggle_output_191"
DEST_PARSER_DIR = BASE_DIR / "data" / "03_parser_outputs" / "mineru" / "03_tai_lieu_chuan_docs" / "en"
CHUNKS_FILE = BASE_DIR / "data" / "06_rag_dataset" / "chunks" / "all_chunks.json"
EMBEDDING_DIR = BASE_DIR / "scratch" / "kaggle_embedding_v2"

try:
    sys.stdout.reconfigure(line_buffering=True)
except Exception:
    pass

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}", flush=True)

def run_cmd(cmd_list, desc):
    log(f"Running: {desc} ({' '.join(cmd_list)})...")
    res = subprocess.run(cmd_list, cwd=str(BASE_DIR), capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        log(f"❌ Error in {desc}: Exit code {res.returncode}")
        log(f"Stdout:\n{res.stdout[-1500:]}")
        log(f"Stderr:\n{res.stderr[-1500:]}")
        raise RuntimeError(f"Step failed: {desc}")
    log(f"✅ Finished: {desc}")
    return res.stdout

def unpack_191(zip_path):
    log(f"Unpacking {zip_path.name} to {DEST_PARSER_DIR}...")
    with zipfile.ZipFile(zip_path, "r") as zf:
        members = zf.namelist()
        for member in members:
            # find entries for EN_PDF_191_Python_3.7_library
            if "EN_PDF_191_Python_3.7_library" in member:
                parts = Path(member).parts
                # locate index where 'EN_PDF_191...' starts
                idx = -1
                for i, p in enumerate(parts):
                    if "EN_PDF_191_Python_3.7_library" in p:
                        idx = i
                        break
                if idx != -1:
                    sub_rel = Path(*parts[idx:])
                    dest = DEST_PARSER_DIR / sub_rel
                    if member.endswith("/"):
                        dest.mkdir(parents=True, exist_ok=True)
                    else:
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        with zf.open(member) as src, open(dest, "wb") as dst:
                            shutil.copyfileobj(src, dst)
    log(f"Extraction of EN_PDF_191 completed into {DEST_PARSER_DIR}!")

def main():
    log("=" * 70)
    log(f"🚀 MONITORING & AUTOMATION PIPELINE FOR {KERNEL_TARGET}")
    log("=" * 70)

    api = KaggleApi()
    api.authenticate()

    start_time = time.time()
    last_status = None
    poll_count = 0

    # Phase 1: Wait for mineru-191-parser
    while True:
        poll_count += 1
        try:
            status_obj = api.kernels_status(KERNEL_TARGET)
            status = getattr(status_obj, "status", None)
            failure = getattr(status_obj, "failure_message", None)
            status_str = str(status)

            elapsed = int(time.time() - start_time)
            elapsed_min = elapsed // 60
            elapsed_sec = elapsed % 60

            if status_str != last_status or poll_count % 3 == 0:
                log(f"Parser Status: {status_str} (Poll #{poll_count}, Elapsed: {elapsed_min}m {elapsed_sec}s)")
                last_status = status_str

            if "COMPLETE" in status_str.upper():
                log(f"🎉 MinerU 191 Parser finished successfully! (Wait time: {elapsed_min}m {elapsed_sec}s)")
                break
            elif "ERROR" in status_str.upper() or "FAIL" in status_str.upper() or failure:
                log(f"❌ Kernel failed: {status_str}, Failure: {failure}")
                sys.exit(1)
        except Exception as e:
            log(f"Warning while polling status: {e}")

        time.sleep(30)

    # Phase 2: Download output
    log("📥 Downloading output files from Kaggle...")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    api.kernels_output(KERNEL_TARGET, path=str(OUTPUT_DIR))
    
    zip_candidates = list(OUTPUT_DIR.glob("*.zip"))
    log(f"Found zip outputs: {[z.name for z in zip_candidates]}")
    zip_path = None
    for z in zip_candidates:
        if "mineru_rag_output" in z.name or "output" in z.name:
            zip_path = z
            break
    if not zip_path and zip_candidates:
        zip_path = zip_candidates[0]

    if zip_path:
        unpack_191(zip_path)
    else:
        log("No zip file found, checking extracted loose files...")
        # Check if loose files exist in OUTPUT_DIR
        loose_md = list(OUTPUT_DIR.rglob("*.md"))
        log(f"Found loose markdown files: {len(loose_md)}")
        for md in loose_md:
            if "EN_PDF_191" in md.name:
                doc_dir = md.parent
                dest_doc = DEST_PARSER_DIR / doc_dir.name
                shutil.copytree(doc_dir, dest_doc, dirs_exist_ok=True)
                log(f"Copied loose document dir to {dest_doc}")

    # Phase 3: Clean & Validate Markdown
    log("🧹 Executing Markdown Cleaning Pipeline v3.0...")
    run_cmd([sys.executable, "scripts/preprocessing/clean_markdown.py", "--execute"], "Clean Markdown")
    run_cmd([sys.executable, "scripts/preprocessing/validate_cleaning.py"], "Validate Cleaning")

    # Phase 4: AST-Aware Chunking & Audit
    log("🧩 Executing AST-Aware & Contextual Chunking Engine...")
    run_cmd([sys.executable, "scripts/rag/chunking_engine.py"], "Chunking Engine")
    run_cmd([sys.executable, "scripts/rag/deep_audit_chunks.py"], "Deep Audit Chunks")

    # Phase 5: Update Kaggle Dataset minhthuy70/embedding
    log("📦 Updating Kaggle dataset minhthuy70/embedding with 100% full chunks...")
    upload_chunk_dir = BASE_DIR / "scratch" / "kaggle_embedding_upload"
    upload_chunk_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(CHUNKS_FILE, upload_chunk_dir / "all_chunks.json")
    api.dataset_create_version(
        folder=str(upload_chunk_dir),
        version_notes="100% complete corpus chunks (323/323 PDFs parsed)",
        dir_mode="zip",
        quiet=False
    )
    time.sleep(15)

    # Phase 6: Launch Dual-Model Embedding Kernel V2
    log("🚀 Launching Kaggle GPU Dual-Model Embedding Kernel V2...")
    EMBEDDING_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(BASE_DIR / "notebooks" / "Kaggle_Embedding_Pipeline_GPU.ipynb", EMBEDDING_DIR / "Kaggle_Embedding_Pipeline_GPU.ipynb")
    meta_embed = {
        "id": "minhthuy70/ai-coding-tutor-embedding-v2",
        "title": "AI Coding Tutor Embedding V2",
        "code_file": "Kaggle_Embedding_Pipeline_GPU.ipynb",
        "language": "python",
        "kernel_type": "notebook",
        "is_private": False,
        "enable_gpu": True,
        "enable_tpu": False,
        "enable_internet": True,
        "keywords": ["gpu", "nlp"],
        "dataset_sources": ["minhthuy70/embedding"],
        "kernel_sources": [],
        "competition_sources": [],
        "model_sources": []
    }
    with open(EMBEDDING_DIR / "kernel-metadata.json", "w", encoding="utf-8") as f:
        import json
        json.dump(meta_embed, f, indent=2)

    res = api.kernels_push(str(EMBEDDING_DIR))
    log(f"✅ Kaggle GPU Embedding Kernel V2 Launched: {res}")
    log("🎉 Pipeline complete. Ready for final ChromaDB vector ingestion!")

if __name__ == "__main__":
    main()
