#!/usr/bin/env python3
import os
import glob
import re

base_dir = "/Users/marsyadiyaulhaq/Downloads/Belajar Kiro/web_inovass/web_inovass"

# Update detail pages
detail_files = glob.glob(os.path.join(base_dir, "layanan-detail-*.html"))
print(f"Updating {len(detail_files)} detail files...\n")

for filepath in detail_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update breadcrumb font size to 0.75rem
        content = re.sub(
            r'font-size:\s*0\.8rem\s*!important',
            'font-size: 0.75rem !important',
            content
        )
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {os.path.basename(filepath)}")
            
    except Exception as e:
        print(f"✗ Error: {os.path.basename(filepath)}: {e}")

# Update layanan pages
layanan_files = glob.glob(os.path.join(base_dir, "layanan-*.html"))
print(f"\nUpdating {len(layanan_files)} layanan files...\n")

for filepath in layanan_files:
    if 'layanan-detail' in filepath:
        continue
        
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update page-breadcrumb if exists
        content = re.sub(
            r'(<nav[^>]*class="page-breadcrumb"[^>]*style="[^"]*font-size:\s*)[^;"]+(;[^"]*")',
            r'\g<1>0.75rem\g<2>',
            content
        )
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {os.path.basename(filepath)}")
            
    except Exception as e:
        print(f"✗ Error: {os.path.basename(filepath)}: {e}")

print("\nDone!")
