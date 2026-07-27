#!/usr/bin/env python3
"""Script to increase spacing after titles 'Dengan' and 'Keunggulan'"""
import re
import glob

# Find all ISO and penyusunan dokumen files
iso_files = glob.glob("layanan-detail-iso-*.html")
penyusunan_files = glob.glob("layanan-detail-penyusunan-dokumen-*.html")
ims_files = ["layanan-detail-ims.html"]
penyusunan_ims = ["layanan-detail-penyusunan-dokumen-ims.html"]

all_files = iso_files + penyusunan_files + ims_files + penyusunan_ims

print(f"Increasing spacing to title sections in {len(all_files)} files...")
print("=" * 50)

for filename in all_files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        
        # Change margin-bottom in benefit-highlight-title from 4rem to 5rem
        pattern1 = r'(\.benefit-highlight-title\s*\{[^}]*margin-bottom:\s*)4rem;'
        if re.search(pattern1, content):
            content = re.sub(pattern1, r'\g<1>5rem;', content)
            modified = True
        
        # Change margin-bottom in iso-benefit-section-title from 3rem to 5rem
        pattern2 = r'(\.iso-benefit-section-title\s*\{[^}]*margin-bottom:\s*)3rem;'
        if re.search(pattern2, content):
            content = re.sub(pattern2, r'\g<1>5rem;', content)
            modified = True
        
        if modified:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Increased spacing in {filename}")
        else:
            print(f"○ No change needed in {filename}")
            
    except Exception as e:
        print(f"✗ Error updating {filename}: {e}")

print("=" * 50)
print("Title spacing increase complete!")
