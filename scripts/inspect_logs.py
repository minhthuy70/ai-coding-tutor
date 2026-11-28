import json
from pathlib import Path

for lf in list(Path('scratch').rglob('*.jsonl')):
    lines = [l for l in lf.read_text(encoding='utf-8').strip().split('\n') if l.strip()]
    dones = []
    for l in lines:
        try:
            ev = json.loads(l)
            if ev.get('event') == 'done':
                dones.append(ev)
        except Exception:
            pass
    if dones:
        total_pages = sum(d.get('pages', 0) for d in dones)
        total_secs = sum(d.get('seconds', 0) for d in dones)
        max_d = max(dones, key=lambda x: x.get('seconds', 0))
        print(lf.name, 'Dones:', len(dones), 'Pages:', total_pages, f'Time: {total_secs/60:.1f}m', f'Speed: {total_pages/total_secs:.2f} p/s')
        print(f"  Longest: {max_d.get('relative_path')} ({max_d.get('pages')} pages in {max_d.get('seconds')}s)")
