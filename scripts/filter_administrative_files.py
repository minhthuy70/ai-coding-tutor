# -*- coding: utf-8 -*-
import fitz
from pathlib import Path
import json

base_dir = Path("data/01_original_documents")
files_to_check = []
for p in base_dir.rglob("*.pdf"):
    if "python_100_authentic_pdfs" in str(p) or "python_batch2_authoritative_pdfs" in str(p):
        files_to_check.append(p)

admin_files = []
quality_files = []

for p in sorted(files_to_check):
    try:
        doc = fitz.open(p)
        pages = len(doc)
        text = ""
        for i in range(min(pages, 10)):
            text += doc[i].get_text() + " "
        doc.close()
        
        text_lower = text.lower()
        
        # Administrative signatures
        is_syllabus = any(term in text_lower for term in [
            "đề cương chi tiết học phần", "đề cương học phần", "chương trình chi tiết môn học",
            "scheme of work", "assessment brief", "tiêu chí chấm điểm", "rubric",
            "kế hoạch giảng dạy", "đề thi giữa học kỳ", "đề kiểm tra giữa học kỳ"
        ])
        
        code_markers = ["def ", "print(", "for ", "while ", "import ", "class "]
        code_count = sum(text.count(marker) for marker in code_markers)
        
        # Link-only or trivial placeholder
        is_placeholder = pages <= 2 and code_count == 0 and ("sharepoint" in text_lower or "drive.google" in text_lower or len(text.strip()) < 200)
        
        # Decision
        if (is_syllabus and code_count < 5) or is_placeholder:
            admin_files.append({
                "path": str(p),
                "filename": p.name,
                "pages": pages,
                "code_count": code_count,
                "sample": " ".join(text[:250].split())
            })
        else:
            quality_files.append({
                "path": str(p),
                "filename": p.name,
                "pages": pages,
                "code_count": code_count
            })
    except Exception as e:
        print(f"Error {p.name}: {e}")

print(f"Total PDFs examined: {len(files_to_check)}")
print(f"Identified administrative/syllabus/placeholder files: {len(admin_files)}")
print(f"High-quality substantive technical files: {len(quality_files)}")
print("\n" + "="*80)
print("DANH SÁCH FILE ĐỀ CƯƠNG / KẾ HOẠCH HỌC TẬP / THI CẦN LOẠI BỎ:")
print("="*80)
for a in admin_files:
    print(f"- {a['filename']} ({a['pages']} trang, code markers: {a['code_count']})")
    print(f"  Nội dung tóm tắt: {a['sample'][:120]}...\n")
