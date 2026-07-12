#!/usr/bin/env python3
import os
import glob
import re

base_dir = "/Users/marsyadiyaulhaq/Downloads/Belajar Kiro/web_inovass/web_inovass"
files = glob.glob(os.path.join(base_dir, "layanan-detail-*.html"))

print(f"Found {len(files)} files to update\n")

for filepath in files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Update detail-page-title inline styles - smaller font
        content = re.sub(
            r'<h1 class="detail-page-title"[^>]*style="[^"]*"[^>]*>',
            '<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important;">',
            content
        )
        
        # If no inline style exists, add it
        content = re.sub(
            r'<h1 class="detail-page-title">',
            '<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important;">',
            content
        )
        
        # Update detail-hero-title inline styles - smaller font
        content = re.sub(
            r'<h1 class="detail-hero-title"[^>]*style="[^"]*"[^>]*>',
            '<h1 class="detail-hero-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important;">',
            content
        )
        
        # If no inline style exists, add it
        content = re.sub(
            r'<h1 class="detail-hero-title">',
            '<h1 class="detail-hero-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important;">',
            content
        )
        
        # Ensure breadcrumb styling is consistent
        if 'detail-breadcrumb-nav' in content:
            # Update breadcrumb-nav
            content = re.sub(
                r'<nav class="detail-breadcrumb-nav"(?![^>]*style=)[^>]*>',
                '<nav class="detail-breadcrumb-nav" style="font-size: 0.8rem !important;">',
                content
            )
            
            # Update breadcrumb links
            content = re.sub(
                r'<a href="[^"]*" class="breadcrumb-link"(?![^>]*style=)[^>]*>',
                lambda m: m.group(0).replace('>', ' style="color: rgba(255, 255, 255, 0.7) !important;">'),
                content
            )
            
            # Update breadcrumb separators
            content = re.sub(
                r'<span class="breadcrumb-sep"(?![^>]*style=)[^>]*>',
                '<span class="breadcrumb-sep" style="color: rgba(255, 255, 255, 0.5) !important;">',
                content
            )
            
            # Update breadcrumb current
            content = re.sub(
                r'<span class="breadcrumb-current"(?![^>]*style=)[^>]*>',
                '<span class="breadcrumb-current" style="color: #00c278 !important; font-weight: 600 !important;">',
                content
            )
        
        elif 'detail-breadcrumb' in content:
            # Update regular breadcrumb
            content = re.sub(
                r'<nav class="detail-breadcrumb"(?![^>]*style=)[^>]*>',
                '<nav class="detail-breadcrumb" style="font-size: 0.8rem !important;">',
                content
            )
            
            # Update links in breadcrumb
            content = re.sub(
                r'(<nav class="detail-breadcrumb"[^>]*>.*?)<a href="([^"]*)"(?![^>]*style=)>',
                r'\1<a href="\2" style="color: rgba(255, 255, 255, 0.7) !important;">',
                content,
                flags=re.DOTALL
            )
            
            # Update spans (separators) 
            content = re.sub(
                r'(<nav class="detail-breadcrumb"[^>]*>.*?)<span>›</span>',
                r'\1<span style="color: rgba(255, 255, 255, 0.5) !important;">›</span>',
                content,
                flags=re.DOTALL
            )
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated {os.path.basename(filepath)}")
        else:
            print(f"- No changes needed for {os.path.basename(filepath)}")
            
    except Exception as e:
        print(f"✗ Error processing {os.path.basename(filepath)}: {e}")

print("\nDone!")
