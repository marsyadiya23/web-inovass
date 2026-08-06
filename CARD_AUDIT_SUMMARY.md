# ⚠️ CARD CONTENT AUDIT - MASALAH DITEMUKAN!

**Status**: 118 Issues Found ❌  
**Files Checked**: 108 files  
**Date**: Context Transfer Session

---

## 🔍 MASALAH UTAMA YANG DITEMUKAN

### 🚨 Issue #1: Generic "sistem manajemen mutu" (111 issues)

**Masalah**: Banyak halaman ISO non-QMS masih menggunakan istilah generic "sistem manajemen mutu" di:
- **Stage 2 Certification Process**: "Verifikasi implementasi sistem manajemen mutu di lapangan"
- **CTA Section**: "Siap Meningkatkan *Sistem Manajemen Mutu* Organisasi Anda?"

**Contoh File Bermasalah**:
- ❌ layanan-detail-iso-39001.html → harus "sistem manajemen keselamatan lalu lintas"
- ❌ layanan-detail-iso-55001.html → harus "sistem manajemen aset"
- ❌ layanan-detail-iso-20000-1.html → harus "sistem manajemen layanan TI"
- ❌ layanan-detail-iso-21001.html → harus "sistem manajemen organisasi pendidikan"
- Dan 107 issues lainnya di berbagai file

---

### 🚨 Issue #2: Generic "mutu" in Benefit Cards (7 issues)

**Masalah**: Beberapa benefit card masih menyebut "mutu" di halaman non-QMS

**File Bermasalah**:
1. ❌ layanan-detail-iso-21001.html
   - Card: "Meningkatkan Mutu Pembelajaran"
   - Card: "Mendukung Perbaikan Berkelanjutan" (menyebut mutu)

2. ❌ layanan-detail-konsultasi-surveillance-iso-22000.html
   - Card: "Evaluasi Objektif Sistem" (desc: efektivitas sistem manajemen mutu)

3. ❌ layanan-detail-konsultasi-surveillance-iso-37301.html
   - Card: "Evaluasi Objektif Sistem" (desc: efektivitas sistem manajemen mutu)

4. ❌ layanan-detail-konsultasi-surveillance-iso-22301.html
   - Card: "Evaluasi Objektif Sistem" (desc: efektivitas sistem manajemen mutu)

5. ❌ layanan-detail-konsultasi-surveillance-iso-37001.html
   - Card: "Evaluasi Objektif Sistem" (desc: efektivitas sistem manajemen mutu)

6. ❌ layanan-detail-konsultasi-surveillance-iso-45001.html
   - Card: "Evaluasi Objektif Sistem" (desc: efektivitas sistem manajemen mutu)

---

## 📊 DISTRIBUSI MASALAH PER KATEGORI

| Kategori | Files Affected | Total Issues |
|----------|----------------|--------------|
| ISO Detail Pages | 13 files | 24 issues |
| **Surveillance Pages** | **19 files** | **57 issues** ⚠️ |
| Penyusunan Dokumen Pages | 16 files | 27 issues |
| Pemeliharaan Pages | 1 file | 2 issues |
| Audit Internal Pages | 1 file | 1 issue |

**Surveillance pages memiliki masalah terbanyak!**

---

## ✅ YANG SUDAH BENAR

- ✅ All CSMS pages (15 pages) - No issues!
- ✅ Most Audit Internal ISO pages (18/19 correct)
- ✅ ISO 9001 pages
- ✅ ISO 13485 pages (correctly uses "mutu alat kesehatan")

---

## 🎯 PERBAIKAN YANG DIPERLUKAN

### Kategori 1: Stage 2 Certification Text
**Pattern**: `Verifikasi implementasi sistem manajemen mutu di lapangan`

**Harus diganti dengan sistem yang sesuai**:
- ISO 14001 → "sistem manajemen lingkungan"
- ISO 45001 → "sistem manajemen K3"
- ISO 27001 → "sistem manajemen keamanan informasi"
- ISO 50001 → "sistem manajemen energi"
- ISO 55001 → "sistem manajemen aset"
- ISO 20000-1 → "sistem manajemen layanan TI"
- ISO 22000 → "sistem manajemen keamanan pangan"
- ISO 22301 → "sistem manajemen kontinuitas bisnis"
- ISO 37001 → "sistem manajemen anti penyuapan"
- ISO 37301 → "sistem manajemen kepatuhan"
- ISO 30301 → "sistem manajemen rekaman"
- ISO 21001 → "sistem manajemen organisasi pendidikan"
- ISO 35001 → "sistem manajemen biorisiko"
- ISO 39001 → "sistem manajemen keselamatan lalu lintas"
- ISO 10002 → "sistem manajemen penanganan keluhan"

### Kategori 2: CTA Section Text
**Pattern**: `Siap Meningkatkan <em>Sistem Manajemen Mutu</em> Organisasi Anda?`

**Harus diganti dengan**:
- ISO 14001 → "Siap Meningkatkan <em>Sistem Manajemen Lingkungan</em> Organisasi Anda?"
- ISO 45001 → "Siap Meningkatkan <em>Sistem Manajemen K3</em> Organisasi Anda?"
- (dan seterusnya sesuai ISO)

### Kategori 3: Benefit Card Descriptions
**Pattern**: "efektivitas sistem manajemen mutu"

**Harus diganti dengan ISO-specific terminology**

---

## 📁 FILE LISTS

### Surveillance Pages dengan Masalah (19 files):
1. layanan-detail-konsultasi-surveillance-iso-14001.html
2. layanan-detail-konsultasi-surveillance-iso-50001.html
3. layanan-detail-konsultasi-surveillance-iso-22000.html
4. layanan-detail-konsultasi-surveillance-iso-10002.html
5. layanan-detail-konsultasi-surveillance-iso-21001.html
6. layanan-detail-konsultasi-surveillance-iso-37301.html
7. layanan-detail-konsultasi-surveillance-iso-39001.html
8. layanan-detail-konsultasi-surveillance-iso-ims.html
9. layanan-detail-konsultasi-surveillance-iso-35001.html
10. layanan-detail-konsultasi-surveillance-iso-13485.html
11. layanan-detail-konsultasi-surveillance-iso-22301.html
12. layanan-detail-konsultasi-surveillance-iso-30301.html
13. layanan-detail-konsultasi-surveillance-iso-27001.html
14. layanan-detail-konsultasi-surveillance-iso-37001.html
15. layanan-detail-konsultasi-surveillance-iso-45001.html
16. layanan-detail-konsultasi-surveillance-iso-55001.html
17. layanan-detail-konsultasi-surveillance-iso-20000-1.html
18. layanan-detail-konsultasi-surveillance-iso-lainnya.html
19. (plus 1 more)

### ISO Detail Pages dengan Masalah (13 files):
1. layanan-detail-iso-39001.html
2. layanan-detail-iso-37301.html
3. layanan-detail-iso-21001.html
4. layanan-detail-iso-10002.html
5. layanan-detail-iso-50001.html
6. layanan-detail-iso-20000-1.html
7. layanan-detail-iso-lainnya.html
8. layanan-detail-iso-55001.html
9. layanan-detail-iso-37001.html
10. layanan-detail-iso-30301.html
11. layanan-detail-iso-13485.html
12. layanan-detail-iso-35001.html
13. (plus more)

### Penyusunan Dokumen Pages dengan Masalah (16 files):
All penyusunan-dokumen-iso-*.html files except ISO 9001

---

## 🚀 READY TO FIX

Semua masalah sudah teridentifikasi dan siap untuk diperbaiki secara batch.

**Next Action**: Lanjutkan perbaikan?

**Estimated Time**: 30-45 minutes untuk fix semua 118 issues
