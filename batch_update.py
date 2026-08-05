#!/usr/bin/env python3
import re

# Data untuk setiap standar ISO
iso_data = {
    '27001': {
        'full_title': 'ISO/IEC 27001 – Sistem Manajemen Keamanan Informasi',
        'year': '2013',
        'breadcrumb': 'Audit Internal ISO/IEC 27001',
        'benefits': ['Melindungi Aset<br>Informasi', 'Mengidentifikasi Ancaman<br>Keamanan', 'Meningkatkan Keamanan<br>Informasi'],
        'description': 'Jasa Audit Internal ISO/IEC 27001:2022 adalah layanan profesional yang membantu organisasi melakukan evaluasi sistematis terhadap efektivitas penerapan Sistem Manajemen Keamanan Informasi, melindungi kerahasiaan, integritas, dan ketersediaan informasi, serta mengidentifikasi risiko keamanan informasi.',
        'cta': 'Keamanan Informasi',
        'cta_desc': 'Konsultasikan kebutuhan audit internal ISO 27001 Anda bersama tim auditor keamanan informasi berpengalaman INOVASS. Kami siap membantu organisasi Anda melindungi aset informasi.'
    },
    '22301': {
        'full_title': 'ISO 22301 – Sistem Manajemen Keberlangsungan Bisnis (BCMS)',
        'year': '2019',
        'breadcrumb': 'Audit Internal ISO 22301',
        'benefits': ['Memastikan Kelangsungan<br>Bisnis', 'Mengidentifikasi Risiko<br>Gangguan', 'Meningkatkan Ketahanan<br>Organisasi'],
        'description': 'Jasa Audit Internal ISO 22301:2019 adalah layanan profesional yang membantu organisasi melakukan evaluasi sistematis terhadap efektivitas penerapan Sistem Manajemen Keberlangsungan Bisnis (BCMS), memastikan kelangsungan operasi saat terjadi gangguan, dan meningkatkan ketahanan organisasi.',
        'cta': 'Keberlangsungan Bisnis',
        'cta_desc': 'Konsultasikan kebutuhan audit internal ISO 22301 Anda bersama tim auditor BCMS berpengalaman INOVASS. Kami siap membantu organisasi Anda meningkatkan ketahanan bisnis.'
    },
    '37001': {
        'full_title': 'ISO 37001 – Sistem Manajemen Anti Penyuapan',
        'year': '2016',
        'breadcrumb': 'Audit Internal ISO 37001',
        'benefits': ['Mencegah Praktik<br>Penyuapan', 'Meningkatkan Integritas<br>Organisasi', 'Kepatuhan Anti<br>Korupsi'],
        'description': 'Jasa Audit Internal ISO 37001:2016 adalah layanan profesional yang membantu organisasi melakukan evaluasi sistematis terhadap efektivitas penerapan Sistem Manajemen Anti Penyuapan, mencegah dan mendeteksi praktik penyuapan, serta meningkatkan integritas dan transparansi organisasi.',
        'cta': 'Sistem Anti Penyuapan',
        'cta_desc': 'Konsultasikan kebutuhan audit internal ISO 37001 Anda bersama tim auditor anti penyuapan berpengalaman INOVASS. Kami siap membantu organisasi Anda mencegah praktik korupsi.'
    },
    '37301': {
        'full_title': 'ISO 37301 – Sistem Manajemen Kepatuhan',
        'year': '2021',
        'breadcrumb': 'Audit Internal ISO 37301',
        'benefits': ['Memastikan Kepatuhan<br>Regulasi', 'Mengurangi Risiko<br>Hukum', 'Meningkatkan Tata<br>Kelola'],
        'description': 'Jasa Audit Internal ISO 37301:2021 adalah layanan profesional yang membantu organisasi melakukan evaluasi sistematis terhadap efektivitas penerapan Sistem Manajemen Kepatuhan, memastikan organisasi mematuhi peraturan dan regulasi yang berlaku, serta mengurangi risiko hukum dan reputasi.',
        'cta': 'Sistem Manajemen Kepatuhan',
        'cta_desc': 'Konsultasikan kebutuhan audit internal ISO 37301 Anda bersama tim auditor kepatuhan berpengalaman INOVASS. Kami siap membantu organisasi Anda meningkatkan kepatuhan regulasi.'
    }
}

for iso_num, data in iso_data.items():
    filename = f'layanan-detail-audit-internal-iso-{iso_num}.html'
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update breadcrumb
        content = re.sub(
            r'Audit Internal ISO/SNI 9001</span>',
            f'{data["breadcrumb"]}</span>',
            content
        )
        
        # Update title  
        content = re.sub(
            r'<title>.*?</title>',
            f'<title>Jasa {data["full_title"]} — INOVASS</title>',
            content
        )
        
        # Update page title
        content = re.sub(
            r'(detail-page-title.*?>).*?(</h1>)',
            f'\\1Jasa Audit Internal {data["full_title"]}\\2',
            content, flags=re.DOTALL
        )
        
        # Update benefits
        content = re.sub(
            r'(benefit-highlight-title">)Dengan Jasa Audit Internal.*?(<)',
            f'\\1Dengan Jasa Audit Internal {data["full_title"].split(" – ")[0]}:{data["year"]} Organisasi Anda Dapat:\\2',
            content
        )
        
        # Update 3 benefit cards
        benefit_pattern = r'(<div class="benefit-highlight-card">\s*<p>).*?(</p>\s*</div>)'
        matches = list(re.finditer(benefit_pattern, content))
        if len(matches) >= 3:
            for i, benefit in enumerate(data['benefits'][:3]):
                content = content[:matches[i].start()] + f'\\1{benefit}\\2' + content[matches[i].end():]
                # Recalculate matches after replacement
                matches = list(re.finditer(benefit_pattern, content))
        
        # Update pengertian
        content = re.sub(
            r'(iso-content-title">)Pengertian Jasa Audit Internal.*?(</h2>)',
            f'\\1Pengertian Jasa Audit Internal {data["full_title"].split(" – ")[0]}:{data["year"]}\\2',
            content
        )
        
        content = re.sub(
            r'(iso-content-desc">\s*)Jasa Audit Internal.*?(?=</p>)',
            f'\\1{data["description"]}',
            content, flags=re.DOTALL
        )
        
        # Update CTA
        content = re.sub(
            r'(Siap Meningkatkan <em>).*?(</em>)',
            f'\\1{data["cta"]}\\2',
            content
        )
        
        content = re.sub(
            r'(page-cta.*?<p>)Konsultasikan.*?(?=</p>)',
            f'\\1{data["cta_desc"]}',
            content, flags=re.DOTALL
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f'✅ Updated {filename}')
        
    except FileNotFoundError:
        print(f'❌ File not found: {filename}')
    except Exception as e:
        print(f'❌ Error updating {filename}: {e}')

print('\n🎉 Batch update completed!')
