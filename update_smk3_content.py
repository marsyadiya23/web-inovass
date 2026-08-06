#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script untuk update konten Target Section dan CTA Section di semua halaman SMK3
"""

import re

# Data untuk setiap halaman SMK3
smk3_pages = {
    'layanan-detail-smk3-gap-analysis.html': {
        'target_title': 'Siapa yang Membutuhkan Gap Analysis SMK3?',
        'target_footer': 'Gap Analysis SMK3 memberikan peta jalan yang jelas untuk implementasi sistem K3 yang efektif, mengidentifikasi kesenjangan antara kondisi saat ini dengan persyaratan PP 50/2012, dan menyusun action plan untuk mencapai compliance dan persiapan sertifikasi yang optimal.',
        'cta_title': 'Gap Analysis SMK3',
        'cta_desc': 'Konsultasikan kebutuhan gap analysis SMK3 Anda bersama tim konsultan berpengalaman INOVASS. Kami siap membantu mengidentifikasi kesenjangan dan menyusun roadmap implementasi SMK3 yang efektif.',
        'target_cards': ['Perusahaan Belum Tersertifikasi', 'Organisasi Persiapan SMK3', 'Perusahaan Audit Temuan Banyak', 'Manufaktur & Pabrikasi', 'Konstruksi & Engineering', 'Oil & Gas, Pertambangan', 'Logistik & Transportasi', 'BUMN & Lembaga Pemerintah', 'Industri Berisiko Tinggi']
    },
    'layanan-detail-smk3-pendampingan-implementasi.html': {
        'target_title': 'Siapa yang Membutuhkan Pendampingan Implementasi SMK3?',
        'target_footer': 'Pendampingan implementasi SMK3 memastikan sistem K3 diterapkan secara efektif di seluruh organisasi, dengan guidance praktis untuk operasionalisasi kebijakan K3, HIRADC, program kerja K3, dan membangun budaya keselamatan untuk mencapai zero accident workplace.',
        'cta_title': 'Implementasi SMK3',
        'cta_desc': 'Konsultasikan kebutuhan implementasi SMK3 Anda bersama tim konsultan berpengalaman INOVASS. Kami siap memberikan pendampingan hands-on untuk implementasi sistem K3 yang efektif di organisasi Anda.',
        'target_cards': ['Perusahaan Implementasi Perdana', 'Organisasi Persiapan Audit', 'Perusahaan Sistem K3 Lemah', 'Manufaktur & Pabrikasi', 'Konstruksi & Engineering', 'Oil & Gas, Pertambangan', 'Logistik & Transportasi', 'BUMN & Lembaga Pemerintah', 'Industri Berisiko Tinggi']
    },
    'layanan-detail-smk3-hiradc.html': {
        'target_title': 'Siapa yang Membutuhkan Jasa HIRADC?',
        'target_footer': 'HIRADC (Hazard Identification, Risk Assessment and Determining Control) merupakan inti dari pengelolaan risiko K3, membantu organisasi mengidentifikasi bahaya di tempat kerja, menilai tingkat risiko, dan menetapkan pengendalian yang efektif untuk mencegah kecelakaan dan penyakit akibat kerja.',
        'cta_title': 'HIRADC',
        'cta_desc': 'Konsultasikan kebutuhan HIRADC Anda bersama tim konsultan K3 berpengalaman INOVASS. Kami siap membantu identifikasi bahaya, penilaian risiko, dan penentuan kontrol yang efektif untuk keselamatan kerja optimal.',
        'target_cards': ['Perusahaan Risiko Tinggi', 'Organisasi Banyak Insiden K3', 'Perusahaan Update Risk Assessment', 'Manufaktur & Pabrikasi', 'Konstruksi & Engineering', 'Oil & Gas, Pertambangan', 'Logistik & Transportasi', 'Chemical & Pharmaceutical', 'Industri Heavy Equipment']
    },
    'layanan-detail-smk3-program-kerja-k3.html': {
        'target_title': 'Siapa yang Membutuhkan Penyusunan Program Kerja K3?',
        'target_footer': 'Program Kerja K3 yang terstruktur dengan baik memberikan panduan operasional untuk implementasi sistem K3, memastikan semua aktivitas K3 direncanakan, dilaksanakan, dan dimonitoring secara sistematis untuk mencapai target zero accident dan compliance berkelanjutan terhadap PP 50/2012.',
        'cta_title': 'Program Kerja K3',
        'cta_desc': 'Konsultasikan kebutuhan penyusunan Program Kerja K3 Anda bersama tim konsultan INOVASS. Kami siap membantu merancang program K3 yang aplikatif dan aligned dengan sasaran keselamatan organisasi Anda.',
        'target_cards': ['Perusahaan Perlu Program K3', 'Organisasi Update Annual Plan', 'Perusahaan Zero Accident Target', 'Manufaktur & Pabrikasi', 'Konstruksi & Engineering', 'Oil & Gas, Pertambangan', 'Logistik & Transportasi', 'BUMN & Lembaga Pemerintah', 'Industri Berisiko Tinggi']
    },
    'layanan-detail-smk3-sasaran-kpi-k3.html': {
        'target_title': 'Siapa yang Membutuhkan Penyusunan Sasaran & KPI K3?',
        'target_footer': 'Sasaran dan KPI K3 yang terukur memungkinkan organisasi untuk memonitor dan mengevaluasi kinerja keselamatan secara objektif, mendorong perbaikan berkelanjutan, dan memastikan pencapaian target zero accident melalui measurement yang sistematis dan data-driven decision making.',
        'cta_title': 'Sasaran & KPI K3',
        'cta_desc': 'Konsultasikan kebutuhan penyusunan sasaran dan KPI K3 Anda bersama tim konsultan INOVASS. Kami siap membantu merancang KPI yang measurable dan aligned dengan strategi K3 organisasi Anda.',
        'target_cards': ['Perusahaan Butuh K3 Metrics', 'Organisasi Performance Tracking', 'Perusahaan Data-Driven K3', 'Manufaktur & Pabrikasi', 'Konstruksi & Engineering', 'Oil & Gas, Pertambangan', 'Logistik & Transportasi', 'BUMN & Lembaga Pemerintah', 'Industri Berisiko Tinggi']
    },
    'layanan-detail-smk3-audit-internal.html': {
        'target_title': 'Siapa yang Membutuhkan Audit Internal SMK3?',
        'target_footer': 'Audit Internal SMK3 yang rutin dan objektif memastikan sistem K3 berjalan efektif, mengidentifikasi gap sebelum audit eksternal, dan memberikan insight untuk perbaikan berkelanjutan sistem K3 guna mempertahankan sertifikasi dan meningkatkan kinerja keselamatan kerja.',
        'cta_title': 'Audit Internal SMK3',
        'cta_desc': 'Konsultasikan kebutuhan audit internal SMK3 Anda bersama tim auditor K3 berpengalaman INOVASS. Kami siap melakukan verifikasi independen dan memberikan rekomendasi perbaikan sistem K3 Anda.',
        'target_cards': ['Perusahaan Tersertifikasi SMK3', 'Organisasi Persiapan Surveillance', 'Perusahaan Perlu Verifikasi', 'Manufaktur & Pabrikasi', 'Konstruksi & Engineering', 'Oil & Gas, Pertambangan', 'Logistik & Transportasi', 'BUMN & Lembaga Pemerintah', 'Industri Berisiko Tinggi']
    },
    'layanan-detail-smk3-tinjauan-manajemen.html': {
        'target_title': 'Siapa yang Membutuhkan Pendampingan Tinjauan Manajemen SMK3?',
        'target_footer': 'Tinjauan Manajemen SMK3 yang efektif memastikan top management terlibat aktif dalam evaluasi kinerja K3, memberikan arahan strategis, dan mengalokasikan sumber daya yang cukup untuk perbaikan berkelanjutan sistem K3 dan pencapaian zero accident workplace.',
        'cta_title': 'Tinjauan Manajemen SMK3',
        'cta_desc': 'Konsultasikan kebutuhan tinjauan manajemen SMK3 Anda bersama tim konsultan INOVASS. Kami siap memfasilitasi management review yang produktif dan menghasilkan action plan untuk peningkatan kinerja K3.',
        'target_cards': ['Perusahaan Tersertifikasi SMK3', 'Organisasi Annual Review', 'Perusahaan Management Engagement', 'Manufaktur & Pabrikasi', 'Konstruksi & Engineering', 'Oil & Gas, Pertambangan', 'Logistik & Transportasi', 'BUMN & Lembaga Pemerintah', 'Industri Berisiko Tinggi']
    },
    'layanan-detail-smk3-persiapan-sertifikasi.html': {
        'target_title': 'Siapa yang Membutuhkan Persiapan Audit Sertifikasi SMK3?',
        'target_footer': 'Persiapan yang matang untuk audit sertifikasi meningkatkan confidence tim, meminimalisir temuan audit, dan memastikan first-time pass rate yang tinggi, menghemat waktu dan biaya re-audit serta mempercepat perolehan sertifikat SMK3 PP 50/2012.',
        'cta_title': 'Persiapan Audit Sertifikasi SMK3',
        'cta_desc': 'Konsultasikan persiapan audit sertifikasi SMK3 Anda bersama tim konsultan INOVASS. Kami siap membantu memastikan kesiapan optimal organisasi Anda menghadapi audit eksternal dengan pre-assessment dan mock audit.',
        'target_cards': ['Perusahaan Menuju Sertifikasi', 'Organisasi First Time Audit', 'Perusahaan Final Preparation', 'Manufaktur & Pabrikasi', 'Konstruksi & Engineering', 'Oil & Gas, Pertambangan', 'Logistik & Transportasi', 'BUMN & Lembaga Pemerintah', 'Industri Berisiko Tinggi']
    },
    'layanan-detail-smk3-pendampingan-sertifikasi.html': {
        'target_title': 'Siapa yang Membutuhkan Pendampingan Audit Sertifikasi SMK3?',
        'target_footer': 'Pendampingan selama audit sertifikasi memberikan support real-time, memfasilitasi komunikasi dengan auditor, dan memastikan proses audit berjalan lancar tanpa hambatan, meningkatkan peluang keberhasilan sertifikasi dan meminimalkan stress tim internal selama audit.',
        'cta_title': 'Pendampingan Audit Sertifikasi SMK3',
        'cta_desc': 'Konsultasikan kebutuhan pendampingan audit sertifikasi SMK3 Anda bersama tim konsultan INOVASS. Kami siap mendampingi organisasi Anda selama proses audit eksternal untuk memastikan kelancaran dan kesuksesan sertifikasi.',
        'target_cards': ['Perusahaan Sedang Audit', 'Organisasi First Time Certification', 'Perusahaan Need Support', 'Manufaktur & Pabrikasi', 'Konstruksi & Engineering', 'Oil & Gas, Pertambangan', 'Logistik & Transportasi', 'BUMN & Lembaga Pemerintah', 'Industri Berisiko Tinggi']
    },
    'layanan-detail-smk3-penyelesaian-temuan.html': {
        'target_title': 'Siapa yang Membutuhkan Penyelesaian Temuan Audit SMK3?',
        'target_footer': 'Penyelesaian temuan audit yang cepat dan efektif merupakan kunci untuk closure audit dan penerbitan sertifikat, memastikan corrective action tepat sasaran mengatasi root cause, dan mencegah recurrence temuan serupa di masa depan untuk sustainability sistem K3.',
        'cta_title': 'Penyelesaian Temuan Audit SMK3',
        'cta_desc': 'Konsultasikan kebutuhan penyelesaian temuan audit SMK3 Anda bersama tim konsultan INOVASS. Kami siap membantu menyusun corrective action yang efektif dan memastikan closure temuan untuk penerbitan sertifikat.',
        'target_cards': ['Perusahaan Ada Temuan Audit', 'Organisasi CAR Submission', 'Perusahaan Finding Closure', 'Manufaktur & Pabrikasi', 'Konstruksi & Engineering', 'Oil & Gas, Pertambangan', 'Logistik & Transportasi', 'BUMN & Lembaga Pemerintah', 'Industri Berisiko Tinggi']
    },
    'layanan-detail-smk3-persiapan-surveillance.html': {
        'target_title': 'Siapa yang Membutuhkan Persiapan Audit Surveillance SMK3?',
        'target_footer': 'Persiapan surveillance audit yang teratur memastikan organisasi mempertahankan compliance berkelanjutan terhadap PP 50/2012, menjaga validitas sertifikat SMK3, dan mendemonstrasikan commitment terhadap perbaikan berkelanjutan sistem K3 untuk keberlanjutan sertifikasi jangka panjang.',
        'cta_title': 'Persiapan Audit Surveillance SMK3',
        'cta_desc': 'Konsultasikan persiapan surveillance audit SMK3 Anda bersama tim konsultan INOVASS. Kami siap membantu mempersiapkan organisasi Anda menghadapi surveillance audit untuk mempertahankan sertifikasi SMK3.',
        'target_cards': ['Perusahaan Tersertifikasi SMK3', 'Organisasi Surveillance Schedule', 'Perusahaan Maintain Certificate', 'Manufaktur & Pabrikasi', 'Konstruksi & Engineering', 'Oil & Gas, Pertambangan', 'Logistik & Transportasi', 'BUMN & Lembaga Pemerintah', 'Industri Berisiko Tinggi']
    },
    'layanan-detail-smk3-pemeliharaan.html': {
        'target_title': 'Siapa yang Membutuhkan Pemeliharaan Penerapan SMK3?',
        'target_footer': 'Pemeliharaan berkelanjutan sistem SMK3 memastikan sistem tetap efektif dan relevan, compliance terjaga sepanjang masa sertifikasi, dan organisasi terus melakukan improvement untuk mencapai excellence dalam kinerja K3 dan zero accident culture yang sustainable.',
        'cta_title': 'Pemeliharaan Penerapan SMK3',
        'cta_desc': 'Konsultasikan kebutuhan pemeliharaan SMK3 Anda bersama tim konsultan INOVASS. Kami siap memberikan dukungan berkelanjutan untuk memastikan sistem K3 tetap efektif dan compliance terjaga sepanjang masa sertifikasi.',
        'target_cards': ['Perusahaan Tersertifikasi SMK3', 'Organisasi Long-term Support', 'Perusahaan Continuous Compliance', 'Manufaktur & Pabrikasi', 'Konstruksi & Engineering', 'Oil & Gas, Pertambangan', 'Logistik & Transportasi', 'BUMN & Lembaga Pemerintah', 'Industri Berisiko Tinggi']
    },
    'layanan-detail-smk3-integrasi-iso.html': {
        'target_title': 'Siapa yang Membutuhkan Integrasi SMK3 dengan ISO?',
        'target_footer': 'Integrasi SMK3 dengan sistem manajemen ISO menghasilkan Integrated Management System yang efisien, mengurangi redundansi dokumentasi dan proses, mengoptimalkan sumber daya, dan menciptakan sinergi antara K3, mutu, dan lingkungan untuk business excellence yang holistic.',
        'cta_title': 'Integrasi SMK3 dengan ISO',
        'cta_desc': 'Konsultasikan kebutuhan integrasi SMK3 dengan sistem ISO Anda bersama tim konsultan INOVASS. Kami siap membantu merancang dan mengimplementasikan Integrated Management System yang efisien dan efektif.',
        'target_cards': ['Perusahaan Multiple Certification', 'Organisasi IMS Implementation', 'Perusahaan Streamline Systems', 'Manufaktur & Pabrikasi', 'Konstruksi & Engineering', 'Oil & Gas, Pertambangan', 'Logistik & Transportasi', 'BUMN & Lembaga Pemerintah', 'Industri Berisiko Tinggi']
    }
}

def update_smk3_file(filename, config):
    """Update target section and CTA section in SMK3 file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern untuk target section title
        target_title_pattern = r'<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">.*?</h2>'
        new_target_title = f'<h2 class="iso-target-section-title" style="margin-bottom: 3rem;">{config["target_title"]}</h2>'
        content = re.sub(target_title_pattern, new_target_title, content)
        
        # Pattern untuk target footer
        target_footer_pattern = r'<p class="iso-target-footer">.*?</p>'
        new_target_footer = f'<p class="iso-target-footer">\n          {config["target_footer"]}\n        </p>'
        content = re.sub(target_footer_pattern, new_target_footer, content, flags=re.DOTALL)
        
        # Pattern untuk CTA title
        cta_title_pattern = r'<h2>Siap .*?<em>.*?</em>.*?</h2>'
        new_cta_title = f'<h2>Siap Meningkatkan <em>{config["cta_title"]}</em> Organisasi Anda?</h2>'
        content = re.sub(cta_title_pattern, new_cta_title, content)
        
        # Pattern untuk CTA description
        cta_desc_pattern = r'(<section class="page-cta">.*?<h2>.*?</h2>\s*<p>).*?(</p>)'
        new_cta_desc = f'\\1{config["cta_desc"]}\\2'
        content = re.sub(cta_desc_pattern, new_cta_desc, content, flags=re.DOTALL)
        
        # Update target cards jika disediakan
        if 'target_cards' in config:
            # Find dan replace semua 9 target cards
            for i, card_text in enumerate(config['target_cards'], 1):
                # Pattern untuk setiap card
                card_pattern = f'(<div class="iso-target-card"><h4>).*?(</h4></div>)'
                
                # Replace hanya untuk card ke-i
                count = 0
                def replacer(match):
                    nonlocal count
                    count += 1
                    if count == i:
                        return f'{match.group(1)}{card_text}{match.group(2)}'
                    return match.group(0)
                
                content = re.sub(card_pattern, replacer, content)
        
        # Write updated content
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Updated: {filename}")
        return True
        
    except Exception as e:
        print(f"✗ Error updating {filename}: {str(e)}")
        return False

# Main execution
if __name__ == "__main__":
    print("Starting SMK3 content update...")
    print("=" * 60)
    
    success_count = 0
    total_count = len(smk3_pages)
    
    for filename, config in smk3_pages.items():
        if update_smk3_file(filename, config):
            success_count += 1
    
    print("=" * 60)
    print(f"Update complete: {success_count}/{total_count} files updated successfully")
