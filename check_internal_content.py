#!/usr/bin/env python3
"""
Script untuk memeriksa konten internal halaman (benefit cards, process steps, dll)
dan memastikan sesuai dengan judul halaman
"""

import os
import re
from pathlib import Path
from collections import defaultdict

def extract_page_info(file_path):
    """Extract page title and main topic from HTML file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Get page title
        title_pattern = r'<title>([^<]+)</title>'
        title_match = re.search(title_pattern, content)
        title = title_match.group(1).strip() if title_match else ""
        title = title.replace('— INOVASS', '').replace('—INOVASS', '').strip()
        
        # Get h1 title
        h1_pattern = r'<h1[^>]*>([^<]+)</h1>'
        h1_match = re.search(h1_pattern, content)
        h1_title = h1_match.group(1).strip() if h1_match else ""
        
        return {
            'file': os.path.basename(file_path),
            'title': title,
            'h1': h1_title,
            'content': content
        }
    except Exception as e:
        return None

def check_generic_qms_content(page_info):
    """Check for generic QMS/ISO 9001 content in non-QMS pages"""
    issues = []
    
    if not page_info:
        return issues
    
    file_name = page_info['file']
    title = page_info['title'].lower()
    content = page_info['content']
    
    # Skip if this IS an ISO 9001/QMS page
    if 'iso 9001' in title or 'iso/sni 9001' in title or 'qms' in title.lower():
        return issues
    
    # Check for generic QMS terminology that shouldn't be in other ISO pages
    problematic_patterns = [
        (r'sistem manajemen mutu(?!\s+alat kesehatan)', 'Generic "sistem manajemen mutu" (should be ISO-specific)'),
        (r'persyaratan ISO 9001:2015', 'Reference to ISO 9001:2015 in wrong page'),
        (r'Manfaat.*ISO 9001(?!3485)', 'Generic ISO 9001 benefit title'),
        (r'Quality Management System(?!\s+\(QMS\))', 'Generic QMS term without context'),
    ]
    
    for pattern, description in problematic_patterns:
        matches = re.finditer(pattern, content, re.IGNORECASE)
        for match in matches:
            # Get context (50 chars before and after)
            start = max(0, match.start() - 50)
            end = min(len(content), match.end() + 50)
            context = content[start:end].replace('\n', ' ')
            
            issues.append({
                'file': file_name,
                'title': page_info['title'],
                'issue_type': 'GENERIC_CONTENT',
                'description': description,
                'matched_text': match.group(),
                'context': context
            })
    
    return issues

def check_benefit_consistency(page_info):
    """Check if benefit cards match the page topic"""
    issues = []
    
    if not page_info:
        return issues
    
    file_name = page_info['file']
    title = page_info['title'].lower()
    content = page_info['content']
    
    # Extract benefit cards
    benefit_pattern = r'<div class="[^"]*benefit[^"]*card[^"]*"[^>]*>\s*<h3>([^<]+)</h3>\s*<p>([^<]+)</p>'
    benefits = re.findall(benefit_pattern, content, re.IGNORECASE)
    
    if not benefits:
        return issues
    
    # Define ISO-specific keywords
    iso_keywords = {
        'iso 14001': ['lingkungan', 'environment', 'ems', 'environmental'],
        'iso 45001': ['k3', 'oh&s', 'keselamatan', 'kesehatan', 'kerja', 'safety', 'health'],
        'iso 27001': ['informasi', 'information', 'security', 'keamanan', 'isms', 'cyber'],
        'iso 22000': ['pangan', 'food', 'fsms', 'safety', 'keamanan pangan'],
        'iso 50001': ['energi', 'energy', 'enms'],
        'iso 55001': ['aset', 'asset', 'ams'],
        'iso 20000': ['ti', 'it', 'layanan', 'service', 'teknologi informasi', 'itsms'],
        'iso 13485': ['alat kesehatan', 'medical device', 'medis'],
        'iso 22301': ['kontinuitas', 'continuity', 'business', 'bcms', 'keberlangsungan'],
        'iso 37001': ['anti', 'suap', 'bribery', 'abms'],
        'iso 37301': ['kepatuhan', 'compliance', 'cms'],
        'iso 30301': ['rekaman', 'arsip', 'records', 'dokumen'],
        'iso 21001': ['pendidikan', 'education', 'sekolah', 'universitas', 'pembelajaran'],
        'iso 35001': ['biorisiko', 'biorisk', 'biosafety', 'biosecurity', 'laboratorium bio'],
        'iso 39001': ['lalu lintas', 'jalan', 'road', 'traffic', 'keselamatan jalan'],
        'iso 10002': ['keluhan', 'complaint', 'pelanggan', 'customer'],
        'csms': ['kontraktor', 'contractor', 'subkontraktor', 'k3 kontraktor'],
        'smk3': ['k3', 'keselamatan', 'kesehatan', 'kerja', 'pp 50'],
    }
    
    # Detect page type
    page_type = None
    for iso_type, keywords in iso_keywords.items():
        if iso_type in title:
            page_type = iso_type
            break
    
    if not page_type:
        return issues
    
    # Check if benefits contain relevant keywords
    relevant_keywords = iso_keywords.get(page_type, [])
    
    for benefit_title, benefit_desc in benefits:
        benefit_text = (benefit_title + ' ' + benefit_desc).lower()
        
        # Check if benefit mentions the right topic
        has_relevant_keyword = any(keyword in benefit_text for keyword in relevant_keywords)
        
        # Check for wrong keywords (e.g., "mutu" in non-QMS page)
        wrong_keywords = []
        if page_type not in ['iso 9001', 'iso 13485']:  # QMS-related
            if 'mutu' in benefit_text and 'alat kesehatan' not in benefit_text:
                wrong_keywords.append('mutu (should be ISO-specific term)')
        
        if wrong_keywords:
            issues.append({
                'file': file_name,
                'title': page_info['title'],
                'issue_type': 'WRONG_TERMINOLOGY',
                'section': 'Benefit Card',
                'card_title': benefit_title,
                'card_desc': benefit_desc[:100],
                'wrong_keywords': wrong_keywords
            })
    
    return issues

def main():
    base_dir = "/Users/marsyadiyaulhaq/Downloads/Belajar Kiro/web_inovass/web_inovass"
    
    print("=" * 80)
    print("INTERNAL CONTENT VERIFICATION")
    print("Checking for generic/mismatched content in detail pages")
    print("=" * 80)
    
    all_issues = defaultdict(list)
    
    # Check specific page categories
    categories = [
        'layanan-detail-iso-*.html',
        'layanan-detail-audit-internal-iso-*.html',
        'layanan-detail-csms-*.html',
        'layanan-detail-pemeliharaan-*.html',
        'layanan-detail-konsultasi-surveillance-iso-*.html',
        'layanan-detail-penyusunan-dokumen-iso-*.html',
    ]
    
    files_checked = 0
    
    for pattern in categories:
        files = list(Path(base_dir).glob(pattern))
        print(f"\n📂 Checking pattern: {pattern} ({len(files)} files)")
        
        for file_path in files:
            files_checked += 1
            page_info = extract_page_info(file_path)
            
            if not page_info:
                continue
            
            # Check for generic content
            generic_issues = check_generic_qms_content(page_info)
            if generic_issues:
                all_issues['generic'].extend(generic_issues)
                print(f"   ⚠️  {file_path.name}: Found {len(generic_issues)} generic content issues")
            
            # Check benefit consistency
            benefit_issues = check_benefit_consistency(page_info)
            if benefit_issues:
                all_issues['benefit'].extend(benefit_issues)
                print(f"   ⚠️  {file_path.name}: Found {len(benefit_issues)} benefit issues")
    
    # Print summary
    print("\n" + "=" * 80)
    print(f"SUMMARY: Checked {files_checked} files")
    print("=" * 80)
    
    total_issues = sum(len(issues) for issues in all_issues.values())
    
    if total_issues == 0:
        print("\n✅ All internal content appears to be consistent!")
    else:
        print(f"\n❌ Found {total_issues} issues:")
        
        if all_issues['generic']:
            print(f"\n📋 GENERIC CONTENT ISSUES ({len(all_issues['generic'])}):\n")
            for i, issue in enumerate(all_issues['generic'][:10], 1):  # Show first 10
                print(f"{i}. {issue['file']}")
                print(f"   {issue['description']}")
                print(f"   Matched: \"{issue['matched_text']}\"")
                print(f"   Context: ...{issue['context']}...")
                print()
        
        if all_issues['benefit']:
            print(f"\n📋 BENEFIT TERMINOLOGY ISSUES ({len(all_issues['benefit'])}):\n")
            for i, issue in enumerate(all_issues['benefit'][:10], 1):  # Show first 10
                print(f"{i}. {issue['file']}")
                print(f"   Card: {issue['card_title']}")
                print(f"   Issue: {', '.join(issue['wrong_keywords'])}")
                print()

if __name__ == "__main__":
    main()
