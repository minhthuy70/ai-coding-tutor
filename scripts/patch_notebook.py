# -*- coding: utf-8 -*-
import json
from pathlib import Path

nb_path = Path("scratch/kaggle_mineru/mineru.ipynb")
nb = json.loads(nb_path.read_text(encoding="utf-8"))

target = "def marked_markdown(middle_path):"
patched = False

for cell in nb["cells"]:
    src = "".join(cell.get("source", []))
    if target in src:
        start = src.find(target)
        end = src.find("def find_file(", start)
        old_block = src[start:end]
        
        # New block with escaped newlines as in WORKER_CODE
        new_block = (
            "def marked_markdown(middle_path):\\n"
            "    try:\\n"
            "        full_data = json.loads(middle_path.read_text(encoding='utf-8'))\\n"
            "        pages = full_data.get('pages', [])\\n"
            "        if len(pages) > 200:\\n"
            "            md_path = middle_path.parent / 'markdown.md'\\n"
            "            if md_path.exists():\\n"
            "                return md_path.read_text(encoding='utf-8')\\n"
            "        parts = []\\n"
            "        base = {k: v for k, v in full_data.items() if k != 'pages'}\\n"
            "        for page in pages:\\n"
            "            page_num = int(page['page_idx']) + 1\\n"
            "            one = {**base, 'pages': [page], 'is_full_document': False}\\n"
            "            page_md = render(load_middle(one), RenderFormat.MARKDOWN)\\n"
            "            page_md = '' if page_md is None else str(page_md).strip()\\n"
            "            marker = f'<!-- page: {page_num} -->'\\n"
            "            parts.append(f'{marker}\\\\n\\\\n{page_md}' if page_md else marker)\\n"
            "        return '\\\\n\\\\n'.join(parts).rstrip() + '\\\\n'\\n"
            "    except Exception:\\n"
            "        md_path = middle_path.parent / 'markdown.md'\\n"
            "        if md_path.exists():\\n"
            "            return md_path.read_text(encoding='utf-8')\\n"
            "        raise\\n\\n\\n"
        )
        src = src[:start] + new_block + src[end:]
        cell["source"] = [src]
        patched = True
        break

if patched:
    nb_path.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding="utf-8")
    print("✅ Successfully patched marked_markdown in notebook!")
else:
    print("❌ Failed to find target function!")
