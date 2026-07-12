#!/usr/bin/env python3
import os
import glob
import re

# Path to the directory
base_dir = "/Users/marsyadiyaulhaq/Downloads/Belajar Kiro/web_inovass/web_inovass"

# Find all layanan-detail-*.html files
files = glob.glob(os.path.join(base_dir, "layanan-detail-*.html"))

print(f"Found {len(files)} files to update")

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern 1: Update detail-header-section with hero background
        # Change background image to hero.png if it uses detail-header-section
        if 'detail-header-section' in content:
            print(f"Processing {os.path.basename(filepath)} (detail-header-section style)...")
            
            # Update breadcrumb styling - make links white/gray, current item green
            content = re.sub(
                r'<nav class="detail-breadcrumb-nav"[^>]*>',
                '<nav class="detail-breadcrumb-nav" style="font-size: 0.8rem !important;">',
                content
            )
            
            content = re.sub(
                r'<a href="[^"]*" class="breadcrumb-link"[^>]*>',
                lambda m: m.group(0).replace('class="breadcrumb-link"', 'class="breadcrumb-link" style="color: rgba(255, 255, 255, 0.7) !important;"') if 'style=' not in m.group(0) else m.group(0),
                content
            )
            
            content = re.sub(
                r'<span class="breadcrumb-sep"[^>]*>',
                '<span class="breadcrumb-sep" style="color: rgba(255, 255, 255, 0.5) !important;">',
                content
            )
            
            content = re.sub(
                r'<span class="breadcrumb-current"[^>]*>',
                '<span class="breadcrumb-current" style="color: #00c278 !important; font-weight: 600 !important;">',
                content
            )
            
            # Update page title - white color, smaller font
            content = re.sub(
                r'<h1 class="detail-page-title"[^>]*>',
                '<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.5rem, 3vw, 2.2rem) !important;">',
                content
            )
            
            # Remove detail-category-badge if exists
            content = re.sub(
                r'<div class="detail-category-badge"[^>]*>.*?</div>\s*',
                '',
                content,
                flags=re.DOTALL
            )
        
        # Pattern 2: Update detail-hero section
        elif 'detail-hero' in content:
            print(f"Processing {os.path.basename(filepath)} (detail-hero style)...")
            
            # Change image to hero.png
            content = re.sub(
                r'<img src="image/[^"]*" alt="[^"]*" class="detail-hero-bg" />',
                '<img src="image/hero.png" alt="Hero background" class="detail-hero-bg" />',
                content
            )
            
            # Update breadcrumb
            content = re.sub(
                r'<nav class="detail-breadcrumb"[^>]*>',
                '<nav class="detail-breadcrumb">',
                content
            )
            
            # Update title - white, smaller
            content = re.sub(
                r'<h1 class="detail-hero-title"[^>]*>',
                '<h1 class="detail-hero-title" style="color: #ffffff !important; font-size: clamp(1.5rem, 3vw, 2.5rem) !important;">',
                content
            )
            
            # Update subtitle - white
            content = re.sub(
                r'<p class="detail-hero-subtitle"[^>]*>',
                '<p class="detail-hero-subtitle" style="color: #ffffff !important; font-size: 0.95rem !important;">',
                content
            )
            
            # Update description - white
            content = re.sub(
                r'<p class="detail-hero-desc"[^>]*>',
                '<p class="detail-hero-desc" style="color: #ffffff !important; font-size: 0.9rem !important;">',
                content
            )
        
        # Only write if content changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Updated {os.path.basename(filepath)}")
        else:
            print(f"  - No changes needed for {os.path.basename(filepath)}")
            
    except Exception as e:
        print(f"  ✗ Error processing {os.path.basename(filepath)}: {e}")

print("\nDone!")
