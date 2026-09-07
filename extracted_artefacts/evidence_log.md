# FORENSIC SEARCH STRATEGY AND EVIDENCE LOG
**Case Name:** Operation Phantom Swipe  
**Target Devices:** Hardware ATM Skimmer (EVD-01) & Suspect Smartphone (EVD-02)  
**Forensic Workstation:** EnCase / Autopsy & Python 3.11 Custom Regex Parser Suite  

---

## 1. FORENSIC SEARCH METHODOLOGY & STRATEGY

To extract digital evidence from the heterogeneous seized media, a multi-stage search strategy was executed:

1. **Raw String & Hex Pattern Indexing:**
   - **Track 2 Magnetic Stripe Regex Pattern:** `;(\d{15,16})=(\d{4}\d+)\?\s*PIN:\s*(\d{4})`
   - Target: Unallocated space, EEPROM dumps (`msr605_dump.raw`), and log files (`track2_data.txt`).

2. **JSON & Structured Application Database Parsing:**
   - Parsed Telegram/WhatsApp sqlite/json exports (`chat_backup.json`) for keyword indicators: `skimmer`, `PIN`, `ATM`, `USDT`, `dumps`, `JCOP`, `vault`.

3. **Geolocation Data Correlation:**
   - Extracted CSV GPS logs (`gps_logs.csv`) and mapped coordinates against target bank ATM kiosks in Delhi (Connaught Place, Karol Bagh) and safehouse locations in Bengaluru.

4. **Cryptocurrency & Merchant Fraud Parsing:**
   - Identified Bitcoin (`bc1q...`) and USDT (`TR7N...`) public addresses, transaction hashes, and e-commerce delivery logs.

---

## 2. SUMMARY OF EXTRACTED ARTEFACT CLASSES (5+ REQUIRED ARTEFACTS)

| Artefact ID | Category | Description / Content Highlights | Evidentiary Significance |
|---|---|---|---|
| **ART-01** | Credit Card Track 2 Dumps | 5 Unique PANs (e.g. `4012888899991234`, `5241999988885678`) with associated PINs (`8492`, `1209`). | Direct proof of ATM skimming and stolen card data collection. |
| **ART-02** | Communication Logs | Chat exchange between `Phantom_Admin` and `Mule_Handler_Delhi` discussing skimmer installation & ₹4,50,000 cash conversion. | Establishes criminal conspiracy (IPC 120B) and role of syndicate leadership. |
| **ART-03** | Geolocation Logs | Timestamped GPS points placing suspect at HDFC ATM Connaught Place during skimmer installation (2026-08-30 13:45 UTC). | Establishes physical presence at the crime scene. |
| **ART-04** | Financial & Crypto Log | BTC Wallet (`bc1qxy2kg...`, Bal: 1.482 BTC) & USDT Wallet (`TR7NHqj...`, Bal: $12,500) + Amazon delivery address. | Demonstrates money laundering flow and illegal proceeds of crime. |
| **ART-05** | Malware/App Metadata | `app_metadata.xml` showing C2 domain `c2.phantom-swipe-net.cc` and BLE target MAC `AA:BB:CC:11:22:33`. | Identifies technical infrastructure and automated exfiltration mechanism. |

---

## 3. AUDIT TRAIL & INTEGRITY STATEMENT
All extracted artefacts were written to `extracted_artefacts/` without mutating original evidence files. All operations were validated against SHA-256 hashes listed in `chain_of_custody/evidence_hashes.sha256`.
