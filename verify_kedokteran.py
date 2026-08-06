#!/usr/bin/env python3
import re

filename = "layanan-detail-k3-lab-pendidikan-kedokteran.html"

print("=" * 80)
print("VERIFIKASI KONTEN K3 LAB PENDIDIKAN KEDOKTERAN")
print("=" * 80)

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check title
    title_match = re.search(r'<title>(.+?)</title>', content)
    if title_match:
        print(f"\n✓ Title: {title_match.group(1)}")
    
    # Required keywords for medical lab
    required = ["kedokteran", "biosafety", "biologis", "patogen", "anatomi", "mikrobiologi", 
                "patologi", "fisiologi", "mahasiswa", "praktikum", "medis", "fakultas"]
    
    print(f"\n✓ KEYWORDS YANG HARUS ADA (Medical Lab):")
    for keyword in required:
        count = len(re.findall(keyword, content, re.IGNORECASE))
        status = "✓" if count > 0 else "❌"
        print(f"  {status} '{keyword}': {count}x")
    
    # Forbidden keywords from road lab
    forbidden = ["aspal", "Marshall", "agregat", "CBR jalan", "bitumen", "penetrasi aspal", 
                 "jalan tol", "material jalan", "transportasi"]
    
    print(f"\n✗ KEYWORDS YANG TIDAK BOLEH ADA (Road Lab):")
    issues = []
    for keyword in forbidden:
        matches = re.findall(keyword, content, re.IGNORECASE)
        if matches:
            issues.append(f"  ❌ '{keyword}': DITEMUKAN {len(matches)}x")
    
    if issues:
        for issue in issues:
            print(issue)
    else:
        print("  ✓ Tidak ada konten road lab yang tertinggal!")
    
    # Check sections
    print(f"\nSECTION CHECKS:")
    sections = [
        ("Benefit Highlight", r'<h2 class="benefit-highlight-title">(.+?)</h2>'),
        ("Pengertian", r'<h2 class="iso-content-title">Pengertian (.+?)</h2>'),
        ("Manfaat", r'<h2 class="iso-benefit-section-title">Manfaat (.+?)</h2>'),
        ("Proses", r'<h2 class="iso-process-title">Proses (.+?)</h2>'),
        ("Target", r'<h2 class="iso-target-section-title"[^>]*>Siapa yang Membutuhkan (.+?)\?</h2>'),
        ("CTA", r'<h2>Siap Meningkatkan <em>(.+?)</em>')
    ]
    
    for section_name, pattern in sections:
        match = re.search(pattern, content, re.DOTALL)
        if match:
            text = match.group(1).strip()
            if "kedokteran" in text.lower() or "medis" in text.lower():
                print(f"  ✓ {section_name}: {text[:60]}...")
            else:
                print(f"  ❌ {section_name}: TIDAK SESUAI - {text[:60]}...")
        else:
            print(f"  ⚠ {section_name}: tidak ditemukan")
    
    # Check breadcrumb parent
    breadcrumb_match = re.search(r'<a href="(layanan-detail-k3-lab-[^"]+)"[^>]*>([^<]+)</a>\s*<span[^>]*>›</span>\s*<span[^>]*>K3 Lab', content)
    if breadcrumb_match:
        print(f"\n✓ Breadcrumb Parent: {breadcrumb_match.group(2)} ({breadcrumb_match.group(1)})")
    
except FileNotFoundError:
    print(f"❌ File tidak ditemukan!")
except Exception as e:
    print(f"❌ Error: {e}")

print(f"\n{'='*80}")
print("VERIFIKASI SELESAI")
print(f"{'='*80}")
