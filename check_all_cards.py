#!/usr/bin/env python3
"""
Script untuk memeriksa semua card di website dan memastikan konten sesuai dengan link tujuan
"""

import os
import re
from pathlib import Path

def extract_card_info(file_path):
    """Extract card information from HTML file"""
    cards_info = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern 1: onclick dengan window.location
        onclick_pattern = r'onclick="window\.location\.href=\'([^\']+)\'"[^>]*>\s*<p>([^<]+)</p>'
        onclick_matches = re.findall(onclick_pattern, content)
        
        for link, text in onclick_matches:
            cards_info.append({
                'file': os.path.basename(file_path),
                'link': link,
                'text': text.strip(),
                'type': 'onclick'
            })
        
        # Pattern 2: anchor tag dengan href
        anchor_pattern = r'<a href="([^"]+)"[^>]*class="product-detail-item[^>]*>\s*<p>([^<]+)</p>'
        anchor_matches = re.findall(anchor_pattern, content)
        
        for link, text in anchor_matches:
            cards_info.append({
                'file': os.path.basename(file_path),
                'link': link,
                'text': text.strip(),
                'type': 'anchor'
            })
            
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    
    return cards_info

def extract_page_title(file_path):
    """Extract main title from the target page"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Try to find h1 title
        title_pattern = r'<h1[^>]*>([^<]+)</h1>'
        match = re.search(title_pattern, content)
        if match:
            return match.group(1).strip()
        
        # Try to find page title in meta or title tag
        meta_pattern = r'<title>([^<]+)</title>'
        match = re.search(meta_pattern, content)
        if match:
            title = match.group(1).strip()
            # Remove "— INOVASS" suffix
            return title.replace('— INOVASS', '').replace('—INOVASS', '').strip()
            
    except:
        pass
    
    return None

def check_card_consistency(base_dir):
    """Check if card text matches the target page title"""
    issues = []
    
    # Get all HTML files
    html_files = list(Path(base_dir).glob('layanan-*.html'))
    
    print(f"Checking {len(html_files)} HTML files...\n")
    
    for html_file in html_files:
        cards = extract_card_info(html_file)
        
        if not cards:
            continue
            
        print(f"\n📄 Checking: {html_file.name}")
        print(f"   Found {len(cards)} cards")
        
        for card in cards:
            # Get target file path
            target_file = Path(base_dir) / card['link']
            
            if not target_file.exists():
                issues.append({
                    'file': card['file'],
                    'issue': 'BROKEN LINK',
                    'card_text': card['text'],
                    'link': card['link']
                })
                print(f"   ❌ BROKEN LINK: {card['link']}")
                continue
            
            # Get target page title
            target_title = extract_page_title(target_file)
            
            if not target_title:
                continue
            
            # Check if card text is similar to target title
            card_text_clean = re.sub(r'\s+', ' ', card['text'].lower())
            target_title_clean = re.sub(r'\s+', ' ', target_title.lower())
            
            # Remove common prefixes for comparison
            prefixes_to_remove = [
                'jasa konsultasi sertifikasi',
                'jasa konsultasi',
                'jasa',
                'layanan'
            ]
            
            card_keywords = card_text_clean
            for prefix in prefixes_to_remove:
                card_keywords = card_keywords.replace(prefix, '').strip()
            
            target_keywords = target_title_clean
            for prefix in prefixes_to_remove:
                target_keywords = target_keywords.replace(prefix, '').strip()
            
            # Check for major mismatches
            # Split into words and check overlap
            card_words = set(card_keywords.split())
            target_words = set(target_keywords.split())
            
            # Calculate similarity (Jaccard index)
            if card_words and target_words:
                intersection = card_words.intersection(target_words)
                union = card_words.union(target_words)
                similarity = len(intersection) / len(union) if union else 0
                
                if similarity < 0.3:  # Less than 30% similarity
                    issues.append({
                        'file': card['file'],
                        'issue': 'MISMATCH',
                        'card_text': card['text'],
                        'target_title': target_title,
                        'link': card['link'],
                        'similarity': f"{similarity*100:.1f}%"
                    })
                    print(f"   ⚠️  MISMATCH ({similarity*100:.1f}%):")
                    print(f"      Card: {card['text'][:60]}...")
                    print(f"      Page: {target_title[:60]}...")
    
    return issues

def main():
    base_dir = "/Users/marsyadiyaulhaq/Downloads/Belajar Kiro/web_inovass/web_inovass"
    
    print("=" * 80)
    print("CARD CONTENT VERIFICATION")
    print("=" * 80)
    
    issues = check_card_consistency(base_dir)
    
    print("\n" + "=" * 80)
    print(f"SUMMARY: Found {len(issues)} potential issues")
    print("=" * 80)
    
    if issues:
        print("\n📋 DETAILED ISSUES:\n")
        for i, issue in enumerate(issues, 1):
            print(f"{i}. File: {issue['file']}")
            print(f"   Issue: {issue['issue']}")
            print(f"   Card Text: {issue['card_text']}")
            if 'target_title' in issue:
                print(f"   Target Title: {issue['target_title']}")
                print(f"   Similarity: {issue['similarity']}")
            print(f"   Link: {issue['link']}")
            print()
    else:
        print("\n✅ All cards appear to be consistent with their target pages!")

if __name__ == "__main__":
    main()
