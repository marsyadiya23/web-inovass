#!/usr/bin/env python3
"""Script to fix breadcrumb for all penyusunan dokumen pages"""
import re
import glob

# Find all penyusunan dokumen files
files = glob.glob("layanan-detail-penyusunan-dokumen-*.html")

print("Fixing breadcrumb for penyusunan dokumen pages...")
print("=" * 50)

for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find the wrong breadcrumb
        old_pattern = r'<a href="layanan-detail-jasa-sertifikasi-iso\.html" class="breadcrumb-link"[^>]*>Jasa Konsultasi Sertifikasi ISO</a>'
        
        # New correct breadcrumb
        new_breadcrumb = '<a href="layanan-detail-penyusunan-dokumen.html" class="breadcrumb-link" style="color: rgba(255, 255, 255, 0.5) !important;">Jasa Penyusunan Dokumen Standar ISO/IEC/SNI</a>'
        
        # Replace if pattern found
        if re.search(old_pattern, content):
            content = re.sub(old_pattern, new_breadcrumb, content)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✓ Fixed breadcrumb in {filename}")
        else:
            print(f"○ Breadcrumb already correct in {filename}")
            
    except Exception as e:
        print(f"✗ Error fixing {filename}: {e}")

print("=" * 50)
print("Breadcrumb fix complete!")
