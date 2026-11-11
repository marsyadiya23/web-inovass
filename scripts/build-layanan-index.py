"""Bangun indeks pencarian Layanan: public/assets/data/layanan.json.

Dijalankan otomatis oleh CI (deploy-cpanel.yml) sebelum zip, jadi indeks selalu sesuai halaman.
Manual: python scripts/build-layanan-index.py
"""
import html
import json
import re
from pathlib import Path

PUBLIC = Path(__file__).resolve().parent.parent / 'public'
LAYANAN = PUBLIC / 'layanan'


def text(fragment: str) -> str:
    return ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', fragment)).split())


def main() -> None:
    # Nama kategori = label tab di halaman kategori (sama di ketujuh halaman)
    tabs = (LAYANAN / 'sertifikasi-organisasi' / 'index.html').read_text(encoding='utf-8')
    labels = {Path(href).parent.name or 'sertifikasi-organisasi': text(label)
              for href, label in re.findall(r'<a href="([^"]+)" class="nav-tab-item[^"]*">\s*<span class="nav-tab-label">(.*?)</span>', tabs, re.S)}

    items = []
    for page in sorted(LAYANAN.glob('*/*.html')):
        if page.name == 'index.html':
            continue
        src = page.read_text(encoding='utf-8')
        m = re.search(r'<h1[^>]*>(.*?)</h1>', src, re.S) or re.search(r'<title>(.*?)</title>', src, re.S)
        title = re.sub(r'\s+—\s+INOVASS$', '', text(m.group(1))) if m else page.stem
        # Induk dari breadcrumb (setelah "Beranda › Layanan"): pembeda judul kembar, mis. 6 halaman "Corrective Action"
        crumbs = [text(c) for c in re.findall(r'class="breadcrumb-link"[^>]*>(.*?)</a>', src, re.S)][2:]
        item = {'t': title, 'c': labels.get(page.parent.name, page.parent.name), 'u': page.relative_to(PUBLIC).as_posix()}
        if crumbs:
            item['p'] = ' › '.join(crumbs)
        items.append(item)

    out = PUBLIC / 'assets' / 'data' / 'layanan.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(items, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    print(f'{len(items)} layanan -> {out.relative_to(PUBLIC.parent)}')


if __name__ == '__main__':
    main()
