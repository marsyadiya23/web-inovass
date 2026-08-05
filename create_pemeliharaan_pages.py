#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script untuk membuat 8 halaman pemeliharaan sistem manajemen ISO
Berdasarkan template surveillance yang sudah ada
"""

import os
import shutil

# Base directory
BASE_DIR = "/Users/marsyadiyaulhaq/Downloads/Belajar Kiro/web_inovass/web_inovass"

# Data untuk setiap standar ISO
STANDARDS = {
    'iso-9001': {
        'code': 'ISO/SNI 9001',
        'year': '2015',
        'title': 'Sistem Manajemen Mutu',
        'benefit_title_highlights': [
            'Memastikan Kesesuaian<br>Berkelanjutan',
            'Menjaga Efektivitas<br>Sistem',
            'Mempertahankan<br>Sertifikasi'
        ],
        'pengertian': 'Jasa Konsultasi Pemeliharaan Sistem Manajemen ISO/SNI 9001:2015 adalah layanan profesional yang membantu organisasi memelihara, memonitor, dan meningkatkan efektivitas sistem manajemen mutu secara berkelanjutan untuk mempertahankan sertifikasi dan performa organisasi.',
        'benefits': [
            {
                'title': 'Pemeliharaan Dokumentasi',
                'desc': 'Membantu update dan pemeliharaan dokumentasi sistem sesuai perubahan proses bisnis'
            },
