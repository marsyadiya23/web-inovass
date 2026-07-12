#!/usr/bin/env python3
import os
import glob
import re
from html import unescape

# Path to the directory
base_dir = "/Users/marsyadiyaulhaq/Downloads/Belajar Kiro/web_inovass/web_inovass"

# Find all layanan-detail-*.html files
files = glob.glob(os.path.join(base_dir, "layanan-detail-*.html"))

print(f"Found {len(files)} files to update\n")

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Extract title from h1 tag (either detail-page-title or detail-hero-title)
        title_match = re.search(r'<h1 class="detail-(?:page|hero)-title"[^>]*>(.*?)</h1>', content, re.DOTALL)
        
        if title_match:
            title_text = title_match.group(1).strip()
            # Clean up HTML entities
            title_text = unescape(title_text)
            # Remove any HTML tags from title
            title_text = re.sub(r'<[^>]+>', '', title_text)
            
            print(f"Processing {os.path.basename(filepath)}")
            print(f"  Title: {title_text}")
            
            # Update breadcrumb-current to match title
            # Pattern 1: For detail-header-section style
            content = re.sub(
                r'(<span class="breadcrumb-current"[^>]*>).*?(</span>)',
                f'\\1{title_text}\\2',
                content,
                flags=re.DOTALL
            )
            
            # Pattern 2: For detail-hero style (last span in breadcrumb)
            content = re.sub(
                r'(<nav class="detail-breadcrumb"[^>]*>.*?<span>›</span>\s*<span[^>]*>).*?(</span>\s*</nav>)',
                f'\\1{title_text}\\2',
                content,
                flags=re.DOTALL
            )
            
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  ✓ Updated breadcrumb\n")
            else:
                print(f"  - Breadcrumb already matches\n")
        else:
            print(f"⚠ Could not find title in {os.path.basename(filepath)}\n")
            
    except Exception as e:
        print(f"✗ Error processing {os.path.basename(filepath)}: {e}\n")

print("Done!")
