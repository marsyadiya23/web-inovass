# 📋 CARD CONTENT AUDIT REPORT

**Date**: Context Transfer Session  
**Total Files Checked**: 108 files  
**Total Issues Found**: 118 issues

---

## 🎯 ISSUE SUMMARY

### Issue Type 1: Generic "sistem manajemen mutu" Text (111 issues)
**Location**: Stage 2 certification process & CTA section  
**Problem**: Many non-QMS ISO pages still use generic "sistem manajemen mutu" terminology

**Affected Files**:
- ISO detail pages (layanan-detail-iso-*.html): 24 issues
- Audit Internal ISO pages: 1 issue
- Pemeliharaan ISO pages: 2 issues
- Surveillance ISO pages: 57 issues
- Penyusunan Dokumen ISO pages: 27 issues

**Should Be Changed To ISO-Specific Terms**:
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
- ISO 13485 → "sistem manajemen mutu alat kesehatan" (CORRECT - keep as is)

---

### Issue Type 2: Generic "mutu" in Benefit Cards (7 issues)
**Location**: Benefit section cards  
**Problem**: Benefit cards mention "mutu" in non-QMS ISO pages

**Affected Files**:
1. layanan-detail-iso-21001.html (2 benefit cards)
2. layanan-detail-konsultasi-surveillance-iso-22000.html (1 card)
3. layanan-detail-konsultasi-surveillance-iso-37301.html (1 card)
4. layanan-detail-konsultasi-surveillance-iso-22301.html (1 card)
5. layanan-detail-konsultasi-surveillance-iso-37001.html (1 card)
6. layanan-detail-konsultasi-surveillance-iso-45001.html (1 card)

---

## 🔧 REQUIRED FIXES

### Priority 1: Fix Stage 2 & CTA "sistem manajemen mutu" Text

**Patterns to Find & Replace**:

1. **In Stage 2 Certification Process**:
   ```html
   OLD: Verifikasi implementasi sistem manajemen mutu di lapangan
   NEW: Verifikasi implementasi [ISO-SPECIFIC SYSTEM] di lapangan
   ```

2. **In CTA Section**:
   ```html
   OLD: <em>Sistem Manajemen Mutu</em>
   NEW: <em>[ISO-SPECIFIC SYSTEM]</em>
   ```

### Priority 2: Fix Benefit Card Terminology

**Files to Fix**:
- layanan-detail-iso-21001.html: Change "Meningkatkan Mutu Pembelajaran" terminology
- Surveillance pages: Fix "Evaluasi Objektif Sistem" descriptions

---

## 📊 BREAKDOWN BY CATEGORY

### A. ISO Detail Pages (layanan-detail-iso-*.html)
**Files with Issues**: 13 files  
**Total Issues**: 24

Most common issues:
- Stage 2 certification text
- CTA section text

### B. Surveillance Pages (layanan-detail-konsultasi-surveillance-iso-*.html)
**Files with Issues**: 19 files  
**Total Issues**: 57

Most common issues:
- Stage 2 text
- CTA section text
- Some benefit cards

### C. Penyusunan Dokumen Pages (layanan-detail-penyusunan-dokumen-iso-*.html)
**Files with Issues**: 16 files  
**Total Issues**: 27

Most common issues:
- Stage 2 text
- CTA section text

### D. Pemeliharaan Pages (layanan-detail-pemeliharaan-iso-*.html)
**Files with Issues**: 1 file  
**Total Issues**: 2

### E. Audit Internal Pages (layanan-detail-audit-internal-iso-*.html)
**Files with Issues**: 1 file  
**Total Issues**: 1

---

## ✅ FILES THAT ARE CORRECT (No Issues Found)

- All CSMS detail pages ✅
- Most Audit Internal ISO pages ✅ (fixed in previous sessions)
- ISO 9001 related pages ✅

---

## 🎯 NEXT STEPS

1. **Create batch fix script** for Stage 2 and CTA text replacements
2. **Manual review** of benefit card descriptions
3. **Verification** after fixes applied
4. **Final audit** to ensure 100% ISO-specific terminology

---

## 📝 NOTES

- ISO 13485 should keep "mutu alat kesehatan" as it's correct ✅
- Be careful not to replace valid uses of "mutu" in QMS contexts
- Each ISO standard needs its own specific terminology
- CTA sections are customer-facing and should be highly accurate

---

**Status**: READY FOR FIX  
**Estimated Time**: ~30-45 minutes for batch processing
