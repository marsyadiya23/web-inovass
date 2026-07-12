#!/usr/bin/env python3
import os
import glob
import re

base_dir = "/Users/marsyadiyaulhaq/Downloads/Belajar Kiro/web_inovass/web_inovass"

# Update detail pages
detail_files = glob.glob(os.path.join(base_dir, "layanan-detail-*.html"))
print(f"Updating {len(detail_files)} detail files to 0.82rem...\n")

for filepath in detail_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update breadcrumb font size to 0.82rem
        content = re.sub(
            r'font-size:\s*0\.(75|9)rem\s*!important',
            'font-size: 0.82rem !important',
            content
        )
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ {os.path.basename(filepath)}")
        else:
            print(f"- {os.path.basename(filepath)} (already correct)")
            
    except Exception as e:
        print(f"✗ Error: {os.path.basename(filepath)}: {e}")

print("\nDone!")
