#!/usr/bin/env python3
import re

files = {
    "layanan-detail-k3-lab-rekayasa-struktur.html": {
        "judul": "K3 Laboratorium Rekayasa Struktur",
        "keywords": ["struktur", "beton", "baja", "compression", "tensile", "UTM", "material testing"],
        "forbidden": ["aspal", "Marshall", "agregat", "jalan", "tanah", "triaxial", "SPT", "hidraulik", "flume"]
    },
    "layanan-detail-k3-lab-rekayasa-tanah.html": {
        "judul": "K3 Laboratorium Rekayasa Tanah (Geoteknik)",
        "keywords": ["tanah", "geoteknik", "SPT", "triaxial", "consolidation", "soil", "CBR tanah"],
        "forbidden": ["aspal", "Marshall", "agregat jalan", "beton struktur", "hidraulik", "flume", "discharge"]
    },
    "layanan-detail-k3-lab-rekayasa-sda.html": {
        "judul": "K3 Laboratorium Sumber Daya Air",
        "keywords": ["hidraulik", "hidrologi", "flume", "discharge", "water", "sediment", "hydraulic"],
        "forbidden": ["aspal", "Marshall", "agregat", "material jalan", "beton struktur", "triaxial", "SPT"]
    }
}

print("=" * 80)
print("VERIFIKASI KONTEN K3 LAB PAGES")
print("=" * 80)

for filename, checks in files.items():
    print(f"\n{'='*80}")
    print(f"FILE: {filename}")
    print(f"JUDUL: {checks['judul']}")
    print(f"{'='*80}")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check title
        title_match = re.search(r'<title>(.+?)</title>', content)
        if title_match:
            print(f"✓ Title: {title_match.group(1)}")
        
        # Check for required keywords
        print(f"\n✓ KEYWORDS YANG HARUS ADA:")
        for keyword in checks['keywords']:
            count = len(re.findall(keyword, content, re.IGNORECASE))
            print(f"  - '{keyword}': ditemukan {count}x")
        
        # Check for forbidden keywords
        print(f"\n✗ KEYWORDS YANG TIDAK BOLEH ADA:")
        issues = []
        for forbidden in checks['forbidden']:
            matches = re.findall(forbidden, content, re.IGNORECASE)
            if matches:
                issues.append(f"  - '{forbidden}': DITEMUKAN {len(matches)}x ❌")
        
        if issues:
            for issue in issues:
                print(issue)
        else:
            print("  ✓ Tidak ada konten yang salah!")
        
        # Check specific sections
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
                if checks['judul'].lower() in text.lower() or any(k in text.lower() for k in checks['keywords'][:3]):
                    print(f"  ✓ {section_name}: {text[:60]}...")
                else:
                    print(f"  ❌ {section_name}: TIDAK SESUAI - {text[:60]}...")
            else:
                print(f"  ⚠ {section_name}: tidak ditemukan")
                
    except FileNotFoundError:
        print(f"❌ File tidak ditemukan!")
    except Exception as e:
        print(f"❌ Error: {e}")

print(f"\n{'='*80}")
print("VERIFIKASI SELESAI")
print(f"{'='*80}")
