# 🔧 AUDIT INTERNAL ISO - FILES NEEDING CUSTOMIZATION

**Issue**: Banyak file masih menggunakan klausul generic ISO 9001 di bagian "Lingkup Audit Internal"
**Impact**: Content tidak spesifik untuk ISO standard yang bersangkutan

---

## ❌ FILES DENGAN GENERIC CONTENT (10 files)

### 1. ISO 55001 – Asset Management ❌
**File**: `layanan-detail-audit-internal-iso-55001.html`
- ❌ Title: "Lingkup Audit Internal ISO 9001" → HARUS: "Lingkup Audit Internal ISO 55001"
- ❌ Cards: Generic ISO 9001 clauses
- ✅ PERLU: Asset Management specific clauses
  - Strategic Asset Management Plan (SAMP)
  - Asset Management Policy
  - Asset Lifecycle Management
  - Asset Portfolio
  - Asset Performance & Condition
  - Risk-Based Asset Management
  - Asset Information Management
  - Stakeholder Engagement
  - Value Creation & Optimization

### 2. ISO 13485 – Medical Devices ❌
**File**: `layanan-detail-audit-internal-iso-13485.html`
- ❌ Generic ISO 9001 clauses
- ✅ PERLU: Medical Device specific clauses
  - Medical Device Design & Development
  - Risk Management (ISO 14971)
  - Regulatory Requirements
  - Sterile Medical Devices
  - Device Master Record (DMR)
  - Design History File (DHF)
  - Post-Market Surveillance
  - Complaint Handling
  - Medical Device Reporting

### 3. ISO 20000-1 – IT Service Management ❌
**File**: `layanan-detail-audit-internal-iso-20000-1.html`
- ❌ Generic ISO 9001 clauses
- ✅ PERLU: ITSM specific clauses
  - Service Management System (SMS)
  - Service Design & Transition
  - Service Delivery Processes
  - Incident & Problem Management
  - Change Management
  - Service Level Management
  - IT Asset Management
  - Service Availability & Continuity
  - Supplier Management

### 4. ISO 21001 – Educational Organizations ❌
**File**: `layanan-detail-audit-internal-iso-21001.html`
- ❌ Generic ISO 9001 clauses
- ✅ PERLU: Education specific clauses
  - Learner-Centered Approach
  - Educational Services Design
  - Learning Environment
  - Curriculum Development
  - Assessment & Evaluation
  - Learning Resources
  - Support for Learners
  - Educator Competence
  - Educational Organization Performance

### 5. ISO 30301 – Records Management ❌
**File**: `layanan-detail-audit-internal-iso-30301.html`
- ❌ Generic ISO 9001 clauses
- ✅ PERLU: Records Management specific clauses
  - Records Management Policy
  - Records System Design
  - Records Creation & Capture
  - Records Classification
  - Records Retention & Disposition
  - Records Security & Protection
  - Metadata Management
  - Records Appraisal
  - Information Governance

### 6. ISO 35001 – Laboratory Biorisk ❌
**File**: `layanan-detail-audit-internal-iso-35001.html`
- ❌ Generic ISO 9001 clauses
- ✅ PERLU: Biorisk specific clauses
  - Biorisk Assessment
  - Biosafety Measures
  - Biosecurity Controls
  - Laboratory Containment
  - Biological Agent Management
  - Emergency Response for Biorisk
  - Personnel Competence in Biorisk
  - Biorisk Communication
  - Incident Investigation

### 7. ISO 39001 – Road Traffic Safety ❌
**File**: `layanan-detail-audit-internal-iso-39001.html`
- ❌ Generic ISO 9001 clauses
- ✅ PERLU: RTS specific clauses
  - Road Traffic Safety Policy
  - RTS Performance Factors
  - Risk Assessment & Treatment
  - Safe System Approach
  - Exposure Management
  - Crash Risk Factors
  - Post-Crash Response
  - Monitoring RTS Performance
  - Stakeholder Engagement

### 8. ISO 10002 – Customer Complaints ❌
**File**: `layanan-detail-audit-internal-iso-10002.html`
- ❌ Generic ISO 9001 clauses
- ✅ PERLU: Complaints specific clauses
  - Complaints Handling Policy
  - Complaint Receipt & Recording
  - Complaint Tracking
  - Complaint Investigation
  - Complaint Resolution
  - Complaint Response
  - Customer Communication
  - Complaint Analysis & Trends
  - Process Improvement

### 9. ISO IMS – Integrated Management System ❌
**File**: `layanan-detail-audit-internal-iso-ims.html`
- ❌ Generic ISO 9001 clauses
- ✅ PERLU: IMS specific clauses
  - Integrated Policy
  - Common Risk Assessment
  - Integrated Objectives
  - Unified Documentation
  - Combined Processes
  - Integrated Monitoring
  - Single Management Review
  - Synergies Between Systems
  - Efficiency Gains

### 10. ISO Lainnya ❌
**File**: `layanan-detail-audit-internal-iso-lainnya.html`
- ❌ Generic ISO 9001 clauses
- ✅ PERLU: Generic but comprehensive clauses
  - Context of Organization
  - Leadership & Commitment
  - Planning & Risk Management
  - Support & Resources
  - Operational Planning & Control
  - Performance Evaluation
  - Internal Audit
  - Management Review
  - Continual Improvement

---

## ✅ FILES ALREADY CUSTOMIZED (9 files)

1. ✅ ISO/SNI 9001 – Quality Management
2. ✅ ISO/SNI 14001 – Environmental Management
3. ✅ ISO 45001 – OH&S Management
4. ✅ ISO 22000 – Food Safety Management
5. ✅ ISO/IEC 27001 – Information Security
6. ✅ ISO 22301 – Business Continuity
7. ✅ ISO 37001 – Anti-Bribery
8. ✅ ISO 37301 – Compliance Management
9. ✅ ISO 50001 – Energy Management

---

## 🎯 ACTION PLAN

### Priority 1: Fix Critical Files (High Usage)
1. ISO 55001 – Asset Management
2. ISO 13485 – Medical Devices
3. ISO 20000-1 – IT Service Management

### Priority 2: Fix Specialized Files
4. ISO 21001 – Educational Organizations
5. ISO 30301 – Records Management
6. ISO 35001 – Laboratory Biorisk

### Priority 3: Fix Niche Files
7. ISO 39001 – Road Traffic Safety
8. ISO 10002 – Customer Complaints
9. ISO IMS – Integrated Management System
10. ISO Lainnya – Other ISO Standards

---

## 📝 TEMPLATE FOR CUSTOMIZATION

Setiap file harus disesuaikan dengan pattern:

```html
<h2 class="iso-target-section-title">Lingkup Audit Internal ISO [NUMBER]</h2>
<div class="iso-target-grid">
  <div class="iso-target-card"><h4>[Clause 1 Specific]</h4></div>
  <div class="iso-target-card"><h4>[Clause 2 Specific]</h4></div>
  ... 9 cards total ...
</div>
<p class="iso-target-footer">
  Audit internal mencakup seluruh klausul ISO [NUMBER]:[YEAR] termasuk [key specific focus areas].
</p>
```

---

**Status**: 10 files need customization
**Estimated Work**: ~30-40 minutes for all files
**Priority**: High - User specifically highlighted this issue

