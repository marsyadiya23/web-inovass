#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create All 16 SMK3 Pages - Complete Script
Generates SMK3 service pages from template with custom content
"""

import os

def apply_replacements(content, replacements):
    """Apply all replacements to content"""
    for old, new in replacements:
        content = content.replace(old, new)
    return content

def create_smk3_page(filename, data):
    """Create one SMK3 page from template"""
    try:
        with open('smk3_template.html', 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Build replacements list
        replacements = [
            # Meta & Navigation
            ('<title>Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu — INOVASS</title>',
             f'<title>{data["title"]} — INOVASS</title>'),
            ('layanan-detail-jasa-perawatan-sistem-sertifikasi.html', 'layanan-detail-smk3.html'),
            ('Jasa Konsultasi Pemeliharaan Sertifikasi Sistem Manajemen ISO/IEC/SNI Organisasi', 'Layanan Konsultasi SMK3'),
            ('<span class="breadcrumb-current" style="color: #00e0a0 !important;">Pemeliharaan ISO/SNI 9001</span>',
             f'<span class="breadcrumb-current" style="color: #00e0a0 !important;">{data["bc"]}</span>'),
            ('<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001 – Sistem Manajemen Mutu</h1>',
             f'<h1 class="detail-page-title" style="color: #ffffff !important; font-size: clamp(1.2rem, 2.5vw, 1.8rem) !important; font-weight: 700 !important;">{data["h1"]}</h1>'),
            
            # Highlights
            ('<h2 class="benefit-highlight-title">Dengan Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 Organisasi Anda Dapat:</h2>',
             f'<h2 class="benefit-highlight-title">{data["ht"]}</h2>'),
            ('            <p>Memastikan Kesesuaian<br>Berkelanjutan</p>', f'            <p>{data["h1t"]}</p>'),
            ('            <p>Menjaga Efektivitas<br>Sistem</p>', f'            <p>{data["h2t"]}</p>'),
            ('            <p>Mempertahankan<br>Sertifikasi</p>', f'            <p>{data["h3t"]}</p>'),
            
            # Pengertian
            ('<h2 class="iso-content-title">Pengertian Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015</h2>',
             f'<h2 class="iso-content-title">{data["pt"]}</h2>'),
            ('Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen mutu secara berkelanjutan untuk mempertahankan sertifikasi dan performa organisasi.',
             data["pd"]),
            
            # Benefits
            ('<h2 class="iso-benefit-section-title">Manfaat Konsultasi Pemeliharaan Sistem Manajemen ISO 9001</h2>',
             f'<h2 class="iso-benefit-section-title">{data["bt"]}</h2>'),
