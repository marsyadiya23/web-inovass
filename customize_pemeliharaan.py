#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script untuk customize konten 11 halaman pemeliharaan
"""
import re

def replace_content(filename, replacements):
    """Replace multiple strings in a file"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Updated: {filename}")

# Data untuk setiap halaman
pages = [
    {
        "file": "layanan-detail-pemeliharaan-iso-50001.html",
        "replacements": [
            # Already partially done, skip for now or add remaining
        ]
    },
    {
        "file": "layanan-detail-pemeliharaan-iso-55001.html",
        "replacements": [
            ("Pemeliharaan ISO/SNI 9001", "Pemeliharaan ISO 55001"),
            ("Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu", 
             "Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 55001 – Sistem Manajemen Aset"),
            ("ISO/SNI 9001:2015", "ISO 55001:2024"),
            ("Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015", 
             "Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO 55001:2024"),
            ("Memastikan Kesesuaian<br>Berkelanjutan", "Optimasi Nilai<br>Aset"),
            ("Menjaga Efektivitas<br>Sistem", "Lifecycle Cost<br>Management"),
            ("Mempertahankan<br>Sertifikasi", "Asset Performance<br>Maksimal"),
        ]
    }
]

print("Starting customization of pemeliharaan pages...")
print("="*60)

for page in pages:
    if page["replacements"]:
        replace_content(page["file"], page["replacements"])

print("="*60)
print("Customization completed!")
