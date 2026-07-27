#!/usr/bin/env python3
"""Script to update titles in penyusunan dokumen pages to match konsultasi format"""
import re
import glob

penyusunan_files = glob.glob("layanan-detail-penyusunan-dokumen-iso-*.html")
penyusunan_files.extend(["layanan-detail-penyusunan-dokumen-ims.html"])

print(f"Updating titles in {len(penyusunan_files)} penyusunan dokumen files...")
print("=" * 50)

for filename in penyusunan_files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified = False
        
        # Extract ISO number from filename
        iso_match = re.search(r'iso-(\d+[-\d]*)', filename)
        ims_match = 'ims' in filename
        lainnya_match = 'lainnya' in filename
        
        if iso_match:
            iso_num = iso_match.group(1)
        elif ims_match:
            iso_num = "IMS"
        elif lainnya_match:
            iso_num = "ISO/IEC/SNI"
        else:
            continue
        
        # Get year and full ISO name from current title
        year_match = re.search(r'ISO[/IEC]*\s*' + re.escape(iso_num.replace('-', '[-/]?')) + r':(\d{4})', content)
        year = year_match.group(1) if year_match else ""
        
        # Construct ISO name
        if iso_num in ["9001", "14001"]:
            iso_name = f"ISO/SNI {iso_num}"
        elif iso_num == "20000-1":
            iso_name = f"ISO/IEC 20000-1"
        elif iso_num in ["27001"]:
            iso_name = f"ISO/IEC {iso_num}"
        elif iso_num == "IMS":
            iso_name = "IMS"
        elif iso_num == "ISO/IEC/SNI":
            iso_name = "ISO/IEC/SNI"
        else:
            iso_name = f"ISO {iso_num}"
        
        iso_full = f"{iso_name}:{year}" if year else iso_name
        
        # 1. Change "Dengan Jasa Penyusunan Dokumen..." to "Dengan ISO..."
        pattern1 = r'(<h2 class="benefit-highlight-title">)Dengan Jasa Penyusunan Dokumen [^:]+:(</h2>)'
        replacement1 = f'\\1Dengan {iso_full} Organisasi Anda Dapat:\\2'
        if re.search(pattern1, content):
            content = re.sub(pattern1, replacement1, content)
            modified = True
        
        # 2. Change "Tentang Layanan Kami" to "Pengertian ISO..."
        pattern2 = r'(<h2 class="iso-content-title">)Tentang Layanan Kami(</h2>)'
        replacement2 = f'\\1Pengertian {iso_full}\\2'
        if re.search(pattern2, content):
            content = re.sub(pattern2, replacement2, content)
            modified = True
        
        # 3. Change "Keunggulan Layanan Penyusunan Dokumen" to "Manfaat Implementasi ISO..."
        pattern3 = r'(<h2 class="iso-benefit-section-title">)Keunggulan Layanan Penyusunan Dokumen(</h2>)'
        if iso_num in ["IMS", "ISO/IEC/SNI"]:
            replacement3 = f'\\1Manfaat Implementasi {iso_num}\\2'
        else:
            replacement3 = f'\\1Manfaat Implementasi ISO {iso_num}\\2'
        if re.search(pattern3, content):
            content = re.sub(pattern3, replacement3, content)
            modified = True
        
        # 5. Change "Proses Penyusunan Dokumen..." to "Proses Sertifikasi ISO..."
        pattern5 = r'(<h2 class="iso-process-title">)Proses Penyusunan Dokumen [^<]+(</h2>)'
        replacement5 = f'\\1Proses Sertifikasi {iso_full}\\2'
        if re.search(pattern5, content):
            content = re.sub(pattern5, replacement5, content)
            modified = True
        
        # 6. Change "Dokumen yang Kami Susun untuk ISO..." to "Siapa yang Harus Menerapkan ISO..."
        pattern6 = r'(<h2 class="iso-target-section-title"[^>]*>)Dokumen yang Kami Susun untuk [^<]+(</h2>)'
        if iso_num in ["IMS", "ISO/IEC/SNI"]:
            replacement6 = f'\\1Siapa yang Membutuhkan {iso_num}?\\2'
        else:
            replacement6 = f'\\1Siapa yang Harus Menerapkan ISO {iso_num}?\\2'
        if re.search(pattern6, content):
            content = re.sub(pattern6, replacement6, content)
            modified = True
        
        if modified:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated titles in {filename}")
        else:
            print(f"○ No changes needed in {filename}")
            
    except Exception as e:
        print(f"✗ Error updating {filename}: {e}")

print("=" * 50)
print("Title update complete!")
print("\nNote: Only titles were changed. Content remains about document preparation services.")
print("If you want to change content to match konsultasi pages, please confirm.")
