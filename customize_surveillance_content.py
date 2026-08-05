#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to customize surveillance page content for 11 ISO standards
Updates benefit section titles, detailed benefits (6 cards), process steps, and scope items
"""

import os
import re

# Define content for each ISO standard
ISO_CONTENT = {
    'iso-50001': {
        'code': 'ISO 50001:2018',
        'title': 'ISO 50001',
        'system': 'Sistem Manajemen Energi',
        'benefit_section_title': 'Manfaat Konsultasi Persiapan Audit Surveillance ISO 50001',
        'benefits': [
            {
                'title': 'Kesiapan Audit Energi',
                'desc': 'Mempersiapkan dokumentasi dan bukti kinerja energi untuk audit surveillance'
            },
            {
                'title': 'Verifikasi EnPI & Baseline',
                'desc': 'Memastikan Energy Performance Indicators dan baseline energi terverifikasi dengan baik'
            },
            {
                'title': 'Review Energy Review',
                'desc': 'Memvalidasi energy review dan identifikasi Significant Energy Uses (SEUs)'
            },
            {
                'title': 'Action Plan Validation',
                'desc': 'Memverifikasi implementasi action plan dan pencapaian target energi'
            },
            {
                'title': 'Data Energi Akurat',
                'desc': 'Menyiapkan data monitoring energi dan measurement & verification yang akurat'
            },
            {
                'title': 'Compliance Energi',
                'desc': 'Memastikan kepatuhan terhadap peraturan energi dan persyaratan ISO 50001'
            }
        ],
        'cta_text': 'Persiapkan Audit Surveillance ISO 50001 Anda Bersama Konsultan Berpengalaman',
        'process_title': 'Proses Konsultasi Persiapan Audit Surveillance ISO 50001',
        'scope_items': [
            'Perusahaan Manufaktur Intensif Energi',
            'Fasilitas Komersial dan Gedung',
            'Industri Petrokimia dan Energi',
            'Transportasi dan Logistik',
            'Data Center dan IT Infrastructure',
            'Hotel dan Hospitality',
            'Rumah Sakit dan Healthcare',
            'Pemerintahan dan Institusi Publik',
            'Semua Organisasi Peduli Efisiensi Energi'
        ]
    },
    'iso-55001': {
        'code': 'ISO 55001:2024',
        'title': 'ISO 55001',
        'system': 'Sistem Manajemen Aset',
        'benefit_section_title': 'Manfaat Konsultasi Persiapan Audit Surveillance ISO 55001',
        'benefits': [
            {
                'title': 'Kesiapan Audit Aset',
                'desc': 'Mempersiapkan dokumentasi SAMP (Strategic Asset Management Plan) untuk audit'
            },
            {
                'title': 'Asset Register Review',
                'desc': 'Memastikan asset register, inventory, dan data kondisi aset ter-update'
            },
            {
                'title': 'Maintenance Records',
                'desc': 'Memvalidasi catatan pemeliharaan dan lifecycle management aset'
            },
