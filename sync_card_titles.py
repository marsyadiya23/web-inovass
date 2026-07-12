#!/usr/bin/env python3
import os
import glob
import re
from html import unescape

base_dir = "/Users/marsyadiyaulhaq/Downloads/Belajar Kiro/web_inovass/web_inovass"

# Step 1: Extract titles from all detail pages
detail_files = glob.glob(os.path.join(base_dir, "layanan-detail-*.html"))
detail_titles = {}

print("=== Extracting titles from detail pages ===\n")

for filepath in detail_files:
    filename = os.path.basename(filepath)
    # Extract the key part (without layanan-detail- and .html)
    key = filename.replace('layanan-detail-', '').replace('.html', '')
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title from h1
        title_match = re.search(r'<h1 class="detail-(?:page|hero)-title"[^>]*>(.*?)</h1>', content, re.DOTALL)
        
        if title_match:
            title_text = title_match.group(1).strip()
            title_text = unescape(title_text)
            title_text = re.sub(r'<[^>]+>', '', title_text)
            detail_titles[key] = title_text
            print(f"{key}: {title_text}")
    except Exception as e:
        print(f"Error reading {filename}: {e}")

print(f"\n=== Found {len(detail_titles)} detail page titles ===\n")

# Step 2: Update card titles in layanan pages
layanan_files = [
    'layanan-iso.html',
    'layanan-sertifikasi.html', 
    'layanan-akreditasi.html',
    'layanan-pelatihan.html'
]

print("=== Updating card titles in layanan pages ===\n")

for layanan_file in layanan_files:
    filepath = os.path.join(base_dir, layanan_file)
    if not os.path.exists(filepath):
        continue
    
    print(f"Processing {layanan_file}...")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        updated_count = 0
        
        # Find all service-item-btn links and update the corresponding h3 titles
        for key, title in detail_titles.items():
            # Pattern: <h3>...</h3> followed by <p>...</p> followed by link to detail page
            pattern = r'(<h3>)(.*?)(</h3>\s*<p>.*?</p>\s*<a href="layanan-detail-' + re.escape(key) + r'\.html")'
            
            def replace_title(match):
                return match.group(1) + title + match.group(3)
            
            new_content = re.sub(pattern, replace_title, content, flags=re.DOTALL)
            
            if new_content != content:
                content = new_content
                updated_count += 1
                print(f"  ✓ Updated card for {key}")
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Total updates in {layanan_file}: {updated_count}\n")
        else:
            print(f"  No updates needed\n")
            
    except Exception as e:
        print(f"  Error: {e}\n")

print("Done!")
