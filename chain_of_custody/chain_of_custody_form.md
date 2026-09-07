# DIGITAL FORENSICS CHAIN OF CUSTODY (CoC) FORM
**Case Name:** Operation Phantom Swipe  
**Case Tracking Number:** DFS-2026-OPSW-009  
**Investigating Unit:** Cyber Crime Investigation Cell (CCIC), Central Bureau of Investigation / State Cyber Cell  
**Lead Investigator:** Parth Bhardwaj, Lead Digital Forensics Examiner (Roll No: 2301730289)  

---

## 1. EVIDENCE SEIZURE SUMMARY

| Item # | Device / Media Description | Serial Number / Hardware ID | Storage Capacity | Physical Condition & Seizure Location | Date & Time (UTC) |
|---|---|---|---|---|---|
| **EVD-01** | MSR-605X Magnetic Stripe Reader/Writer & Skimmer Overlay PCB | MSR605-2025-9082 | 4 MB Flash EEPROM | Intact hardware skimmer extracted from ATM Kiosk, Block C, Connaught Place, New Delhi. Secured in static-shielding bag. | 2026-09-02 04:12:00 |
| **EVD-02** | Phantom Android Smartphone (OnePlus 11 5G) | IMEI-1: 864209041234567<br>IMEI-2: 864209041234568 | 256 GB NVMe UFS 3.1 | Active touch screen unlocked at scene, battery 84%, placed in Faraday Isolation Shield Bag. | 2026-09-02 04:45:00 |

---

## 2. EVIDENCE CUSTODY TRANSFER LOG

| Item # | Relinquished By (Name & Title) | Received By (Name & Title) | Date & Time | Purpose of Transfer | Transfer Location / Facility | Verification Hash Checked? |
|---|---|---|---|---|---|---|
| **EVD-01** | Sub-Inspr. V. Rao (Seizing Officer) | Inspr. S. Sharma (Forensic Lead) | 2026-09-02 06:30 | Transport from Crime Scene to Forensic Lab | CCIC Evidence Vault Room 102 | Yes (SHA-256 Initial) |
| **EVD-01** | Inspr. S. Sharma (Forensic Lead) | Tech. Asst. A. Verma (Imaging Analyst) | 2026-09-02 08:00 | Hardware Write-Blocker Attachment & Bit-Stream EEPROM Extraction | Digital Forensics Lab Station 4 | Yes (Pre/Post Hash Match) |
| **EVD-02** | Sub-Inspr. V. Rao (Seizing Officer) | Inspr. S. Sharma (Forensic Lead) | 2026-09-02 06:30 | Transport in Signal Blocking Shield Bag | CCIC Evidence Vault Room 102 | Yes (SHA-256 Initial) |
| **EVD-02** | Inspr. S. Sharma (Forensic Lead) | Sr. Analyst R. Gupta (Mobile Forensics) | 2026-09-02 09:15 | Logical & Physical Acquisition via Write-Blocked Mobile Workstation | Digital Forensics Lab Station 2 | Yes (Pre/Post Hash Match) |

---

## 3. EVIDENCE CRYPTOGRAPHIC INTEGRITY MANIFEST (SHA-256)

All evidence files generated during the bit-stream bit-for-bit acquisition were immediately hashed using SHA-256 prior to analysis.

| Item # | File Relative Path | SHA-256 Hash Digest | File Size (Bytes) | Verification Status |
|---|---|---|---|---|
| EVD-01.1 | `evidence/skimmer_device/msr605_dump.raw` | `0bd8fc1fe19e52b0e3252ff7f39adaae9f4c068bce3db981b8fa9b849117062a` | 85 | Verified Intact |
| EVD-01.2 | `evidence/skimmer_device/track2_data.txt` | `b6069b4849181c862053a7f082d1c8164946dbdbfdeee5f2da931f3687992eb0` | 557 | Verified Intact |
| EVD-02.1 | `evidence/suspect_phone/chat_backup.json` | `8ff63776610a004a1c86c83ae1cb7d116aa6d29572551651412c805141dcff2d` | 2,130 | Verified Intact |
| EVD-02.2 | `evidence/suspect_phone/gps_logs.csv` | `ba1e81b70ca0565381e58da94625796bd01dc913aff336320ca6a382024955a7` | 509 | Verified Intact |
| EVD-02.3 | `evidence/suspect_phone/transaction_history.json` | `5b05f78e5d77f25a4b398894883a53f7d3fc081125b4961f2fe4dd1f8e82f7da` | 1,328 | Verified Intact |
| EVD-02.4 | `evidence/suspect_phone/app_metadata.xml` | `4a3f16d810aba1a5be317853349c6ba79f2ec097d60f2aa66d744b1410b61882` | 423 | Verified Intact |
| EVD-02.5 | `cryptography/encrypted_vault.zip` | `24a1a6720a3d13f023f0d3d745427df46431ae2756548e8ceb0c46f97e721e92` | 586 | Verified Intact |

---

## 4. AUTHORIZATION AND FINAL SIGN-OFF

- **Seizing Officer Signature:** `Sub-Inspr. V. Rao` (Date: 2026-09-02)
- **Lead Examiner Signature:** `Inspr. S. Sharma` (Date: 2026-09-02)
- **Laboratory Director Clearance:** `Dr. A. K. Roy, Chief Forensic Scientist` (Date: 2026-09-02)
