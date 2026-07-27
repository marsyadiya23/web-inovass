#!/usr/bin/env python3
"""Script to add spacing after titles 'Dengan' and 'Keunggulan'"""
import re
import glob

# Find all ISO and penyusunan dokumen files
iso_files = glob.glob("layanan-detail-iso-*.html")
penyusunan_files = glob.glob("layanan-detail-penyusunan-dokumen-*.html")
ims_files = ["layanan-detail-ims.html", "layanan-detail-iso-lainnya.html"]
penyusunan_ims = ["layanan-detail-penyusunan-dokumen-ims.html", "layanan-detail-penyusunan-dokumen-iso-lainnya.html"]

all_files = iso_files + penyusunan_files + ims_files + penyusunan_ims

print(f"Adding spacing to title sections in {len(all_files)} files...")
print("=" * 50)

for filename in all_files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        
        # Pattern 1: Find benefit-highlight-title and add margin-bottom
        pattern1 = r'\.benefit-highlight-title\s*\{([^}]*)\}'
        
        def replace_benefit_title(match):
            styles = match.group(1)
            # Check if margin-bottom already exists
            if 'margin-bottom' not in styles:
                # Add margin-bottom before the closing brace
                new_styles = styles.rstrip() + '\n      margin-bottom: 4rem;'
                return f'.benefit-highlight-title {{{new_styles}\n    }}'
            return match.group(0)
        
        new_content = re.sub(pattern1, replace_benefit_title, content)
        if new_content != content:
            modified = True
            content = new_content
        
        # Pattern 2: Find iso-benefit-section-title and add margin-bottom
        pattern2 = r'\.iso-benefit-section-title\s*\{([^}]*)\}'
        
        def replace_benefit_section(match):
            styles = match.group(1)
            # Check if margin-bottom already exists
            if 'margin-bottom' not in styles:
                # Add margin-bottom
                new_styles = styles.rstrip() + '\n      margin-bottom: 3rem;'
                return f'.iso-benefit-section-title {{{new_styles}\n    }}'
            return match.group(0)
        
        new_content = re.sub(pattern2, replace_benefit_section, content)
        if new_content != content:
            modified = True
            content = new_content
        
        if modified:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Added spacing to {filename}")
        else:
            print(f"○ Spacing already present in {filename}")
            
    except Exception as e:
        print(f"✗ Error updating {filename}: {e}")

print("=" * 50)
print("Title spacing update complete!")
