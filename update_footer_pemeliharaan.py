#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update Footer Text Script for Pemeliharaan Pages
This script will update the iso-target-footer text to be specific for each ISO standard
"""

def update_footer(filename, new_footer_text):
    """Update footer text in a file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Generic footer text to replace
        old_footer = 'Konsultasi pemeliharaan mencakup dukungan berkelanjutan untuk menjaga efektivitas sistem, compliance, dan kesiapan audit surveillance/recertification.'
        
        if old_footer in content:
            content = content.replace(old_footer, new_footer_text)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ {filename}: Footer updated successfully")
            return True
        else:
            print(f"⚠️  {filename}: Generic footer not found (might be already customized)")
            return False
    except Exception as e:
        print(f"❌ Error in {filename}: {e}")
        return False

# =============================================================================
# FOOTER TEXT DATA FOR 11 FILES
# =============================================================================

footer_data = {
    'layanan-detail-pemeliharaan-iso-9001.html': 
        'Konsultasi pemeliharaan mencakup dukungan monitoring quality performance, process effectiveness, dan kesiapan QMS audit surveillance/recertification.',
    
    'layanan-detail-pemeliharaan-iso-50001.html': 
        'Konsultasi pemeliharaan mencakup dukungan monitoring energy performance, EnPI tracking, SEU management, dan kesiapan EnMS audit surveillance/recertification.',
    
    'layanan-detail-pemeliharaan-iso-55001.html': 
        'Konsultasi pemeliharaan mencakup dukungan monitoring asset performance, lifecycle management, asset health, dan kesiapan AMS audit surveillance/recertification.',
    
    'layanan-detail-pemeliharaan-iso-21001.html': 
        'Konsultasi pemeliharaan mencakup dukungan monitoring learning outcomes, stakeholder satisfaction, educational performance, dan kesiapan EOMS audit surveillance/recertification.',
    
    'layanan-detail-pemeliharaan-iso-13485.html': 
        'Konsultasi pemeliharaan mencakup dukungan monitoring post-market surveillance, CAPA effectiveness, regulatory compliance, dan kesiapan MDQMS audit surveillance/recertification.',
    
    'layanan-detail-pemeliharaan-iso-39001.html': 
        'Konsultasi pemeliharaan mencakup dukungan monitoring road safety performance, accident/incident trends, driver competence, dan kesiapan RTSMS audit surveillance/recertification.',
    
    'layanan-detail-pemeliharaan-iso-10002.html': 
        'Konsultasi pemeliharaan mencakup dukungan monitoring complaint handling performance, resolution effectiveness, customer satisfaction, dan kesiapan CHMS audit surveillance/recertification.',
    
    'layanan-detail-pemeliharaan-iso-30301.html': 
        'Konsultasi pemeliharaan mencakup dukungan monitoring records lifecycle, retention compliance, metadata management, dan kesiapan MSR audit surveillance/recertification.',
    
    'layanan-detail-pemeliharaan-iso-20000-1.html': 
        'Konsultasi pemeliharaan mencakup dukungan monitoring service delivery, SLA performance, incident management, dan kesiapan SMS audit surveillance/recertification.',
    
    'layanan-detail-pemeliharaan-ims.html': 
        'Konsultasi pemeliharaan mencakup dukungan monitoring integrated system performance, multi-standard compliance, synergy effectiveness, dan kesiapan IMS audit surveillance/recertification.',
    
    'layanan-detail-pemeliharaan-lainnya.html': 
        'Konsultasi pemeliharaan mencakup dukungan berkelanjutan untuk monitoring system effectiveness, compliance requirements sesuai standard yang diterapkan, dan kesiapan audit surveillance/recertification.',
    
    'layanan-detail-pemeliharaan-iso-35001.html': 
        'Konsultasi pemeliharaan mencakup dukungan monitoring biorisk assessment, containment measures, emergency response, dan kesiapan BMS audit surveillance/recertification.',
}

# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    print("="*80)
    print("UPDATE FOOTER TEXT SCRIPT - Pemeliharaan Pages")
    print("="*80)
    print(f"\nThis script will update footer text in {len(footer_data)} files")
    print("Please wait...\n")
    
    success_count = 0
    failed_files = []
    
    for filename, footer_text in footer_data.items():
        print(f"\nProcessing: {filename}")
        print("-" * 80)
        
        if update_footer(filename, footer_text):
            success_count += 1
        else:
            failed_files.append(filename)
    
    print("\n" + "="*80)
    print("FOOTER UPDATE COMPLETE")
    print("="*80)
    print(f"\n✅ Successfully updated: {success_count}/{len(footer_data)} files")
    
    if failed_files:
        print(f"\n⚠️  Files that need manual check:")
        for f in failed_files:
            print(f"   - {f}")
    else:
        print("\n🎉 All footer texts successfully updated!")
    
    print("\n" + "="*80)
