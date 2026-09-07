# FORENSIC INVESTIGATION REPORT & LEGAL-TECHNICAL ANALYSIS
## OPERATION PHANTOM SWIPE: CROSS-BORDER ATM SKIMMING & CREDIT CARD FRAUD RING

**Case File Reference:** DFS-2026-OPSW-009  
**Investigating Authority:** Digital Forensics & Cyber Crime Division, Central Bureau of Investigation  
**Lead Investigator / Author:** Parth Bhardwaj (Roll No: 2301730289)  
**Date of Issue:** September 7, 2026  
**Classification:** HIGHLY CONFIDENTIAL / LAW ENFORCEMENT RESTRICTED  

---

### EXECUTIVE SUMMARY

Operation Phantom Swipe was launched following an automated fraud anomaly detection alert triggered by major Indian banking institutions (HDFC Bank, State Bank of India) regarding unauthorized Track 2 magnetic stripe card cloning and high-frequency cash withdrawals across ATM kiosks in New Delhi and Bengaluru.

A joint task force seized two primary physical digital evidence items:
1. **EVD-01:** An MSR-605X magnetic stripe reader/writer hardware skimmer board fitted with a custom PIN pad camera overlay.
2. **EVD-02:** A mobile smartphone belonging to primary suspect Victor K. (alias `@Phantom_Admin`).

Bit-stream forensic acquisition, cryptographic hash verification (SHA-256), regex-based media analysis, and dictionary password recovery were executed under ISO/IEC 27037 and NIST SP 800-86 standards. Forensic evidence confirmed a cross-border syndicate operating across India, Eastern Europe, and cloud-hosted C2 servers. Stolen credit card track data was converted into cloned physical cards (JCOP smart cards) and exfiltrated into cryptocurrency wallets (BTC, USDT) totaling ₹68.5 Lakhs.

---

### SECTION 1: CYBERCRIME CLASSIFICATION & TAXONOMY

#### 1.1 Scenario Analysis and Offence Identification
The investigation identified five distinct criminal operational vectors:
1. **ATM Skimmer Installation & Hardware Tampering:** Physical attachment of magnetic stripe reading heads (Track 2 reader) and micro-pinhole cameras onto public ATM bezels.
2. **Magnetic Stripe Card Cloning & Counterfeiting:** Encoding harvested Track 1/Track 2 data onto blank magnetic stripe / Java JCOP cards for unauthorized cash withdrawals.
3. **Card-Not-Present (CNP) Online Fraud:** Utilizing stolen PANs, CVVs, and expiry dates to execute e-commerce transactions.
4. **Command & Control (C2) Data Exfiltration:** Transmitting intercepted card records over encrypted Bluetooth Low Energy (BLE) and HTTPS channels to cloud-hosted infrastructure (`c2.phantom-swipe-net.cc`).
5. **Cryptocurrency Money Laundering & Mule Network:** Transferring illicit cash withdrawals into Tether (USDT) and Bitcoin to obfuscate financial audit trails.

#### 1.2 Comprehensive Cybercrime Taxonomy Matrix

| Cybercrime Class | Sub-Technique / Vector | Primary Target | Forensic Evidence Found | Primary Impact |
|---|---|---|---|---|
| **ATM Skimming** | Magnetic head interception + PIN pad overlay camera | Financial Institutions & Bank Customers | `msr605_dump.raw`, `track2_data.txt` | Direct compromise of payment card credentials |
| **Identity Theft & Forgery** | Magnetic track encoding on blank JCOP cards | Card Issuers & Cardholders | Extracted Track 2 logs with cleartext PINs | Financial loss, unauthorized identity representation |
| **Wire & Online Fraud** | CNP e-commerce transactions | E-commerce Merchants | `transaction_history.json` (Amazon orders) | Unauthorized financial asset conversion |
| **Cyber Espionage / System Access** | Unauthorized BLE/C2 socket communication | Commercial Bank ATM Kiosks | `app_metadata.xml` (C2 server URL & BLE MAC) | Infrastructure integrity breach |
| **Money Laundering** | Crypto conversion via peer-to-peer mule network | Financial Regulatory System | BTC/USDT transaction logs in chat backup | Obfuscation of illicit proceeds of crime |

#### 1.3 Statutory Mapping under Indian and International Law

```
                                    ┌────────────────────────────────────────────────────────┐
                                    │               OPERATION PHANTOM SWIPE                  │
                                    └──────────────────────────┬─────────────────────────────┘
                                                               │
         ┌─────────────────────────────────────────────────────┼─────────────────────────────────────────────────────┐
         ▼                                                     ▼                                                     ▼
┌──────────────────────────────┐                   ┌──────────────────────────────┐                   ┌──────────────────────────────┐
│     INDIAN IT ACT (2000)     │                   │     INDIAN PENAL CODE (IPC)  │                   │      BUDAPEST CONVENTION     │
├──────────────────────────────┤                   ├──────────────────────────────┤                   ├──────────────────────────────┤
│ • Sec 43: Unauthorized Access│                   │ • Sec 419: Cheating by Person│                   │ • Art 2: Illegal Access      │
│ • Sec 66: Computer Hacking   │                   │ • Sec 420: Cheating & Property│                  │ • Art 3: Illegal Interception│
│ • Sec 66C: Identity Theft    │                   │ • Sec 468: Forgery for Cheating│                 │ • Art 4: Data Interference   │
│ • Sec 66D: Personation Fraud │                   │ • Sec 471: Using Forged Record│                  │ • Art 6: Device Misuse       │
│ • Sec 66F: Cyber Terrorism   │                   │ • Sec 120B: Criminal Conspiracy│                 │ • Art 23-35: International MLA│
└──────────────────────────────┘                   └──────────────────────────────┘                   └──────────────────────────────┘
```

##### A. Indian Information Technology Act, 2000 (Amended 2008) Statutory Definitions & Provisions
- **Section 2(t) [Electronic Record]:** Defines data, record or data generated, image or sound stored, received or sent in an electronic form or micro film or computer generated micro fiche.
- **Section 2(r) [Electronic Form]:** Information generated, sent, received or stored in media, magnetic, optical, computer memory, or similar device.
- **Section 2(v) [Information]:** Includes data, message, text, images, sound, voice, codes, computer programmes, software, and databases.
- **Section 2(o) [Data]:** Representation of information, knowledge, facts, concepts, or instructions prepared in a formalized manner.
- **Section 2(k) & 2(i) [Computer Resource & Computer]:** Encompasses high-speed data processing devices, systems, networks, and databases.
- **Section 43 (Penalty for damage to computer system):** Applies to unauthorized extraction and copying of card track data from bank ATM terminals.
- **Section 66 (Computer Related Offences):** Penalizes fraudulent or dishonest interception and manipulation of computer data (skimmer hardware insertion).
- **Section 66C (Punishment for identity theft):** Directly maps to harvesting payment card numbers, electronic signatures, and unique PIN codes (`PIN: 8492`).
- **Section 66D (Punishment for cheating by personation using computer resource):** Applies to using cloned cards to personate legitimate account holders at ATM kiosks.
- **Section 66E (Violation of privacy):** Applies to capturing PIN pad keystrokes and victim images via pinhole cameras.

##### B. Bharatiya Nyaya Sanhita (BNS 2023) / Indian Penal Code (IPC 1860)
- **Section 319 / Sec 419 IPC (Cheating by personation):** Impersonating account holders to withdraw cash.
- **Section 318 / Sec 420 IPC (Cheating and dishonestly inducing delivery of property):** Fraudulent acquisition of cash from bank ATM vaults.
- **Section 336 / Sec 468 IPC (Forgery for purpose of cheating):** Creating counterfeit magnetic stripe payment cards.
- **Section 340 / Sec 471 IPC (Using as genuine a forged document/electronic record):** Inserting forged cloned cards into ATM card readers.
- **Section 61 / Sec 120B IPC (Criminal Conspiracy):** Multi-person syndicate planning between `@Phantom_Admin` and regional mule handlers.

##### C. Indian Evidence Act (IEA 1872) / BSA 2023 & Landmark Judicial Precedents
- **Section 65A & 65B IEA / Section 63 BSA 2023 (Admissibility of Electronic Records):** Mandates special certificate procedure for secondary electronic evidence.
- ***Anvar P.V. v. P.K. Basheer (2014) 10 SCC 473:*** The Supreme Court held that electronic evidence can only be proved in accordance with Section 65B, overriding general secondary evidence provisions under Section 65.
- ***Arjun Panditrao Khotkar v. Kailash Kushanrao Gorantyal (2020) 7 SCC 1:*** Clarified that a Section 65B(4) certificate is a mandatory condition precedent for admissibility of secondary electronic records whenever the original physical device cannot be produced in court.
- ***State of Karnataka v. Hiremath (2019) 7 SCC 515:*** Ruled that non-furnishing of a 65B certificate at the chargesheet stage is curable before trial begins.
- ***P. Gopalakrishnan @ Dileep v. State of Kerala (2020) 9 SCC 161:*** Established that contents of memory cards/pen-drives are electronic records (documents), and cloned copies must be furnished to the accused for effective defence.
- ***Selvi v. State of Karnataka (2010) 7 SCC 263:*** Held that involuntary administration of scientific techniques violates fundamental rights under Article 20(3) (self-incrimination).

##### D. International Budapest Convention on Cybercrime (ETS No. 185)
- **Article 2 (Illegal Access):** Accessing ATM internal bus or magnetic head signal lines without right.
- **Article 3 (Illegal Interception):** Technical interception of non-public transmissions of payment card data.
- **Article 6 (Misuse of Devices):** Production, sale, and distribution of skimming hardware (MSR-605X) and skimming controller apps (`ATM_Ghost_v3.2`).
- **Article 14–21 (Procedural Law):** Expedited preservation of stored computer data and real-time collection of traffic data.
- **Article 23–35 (International Cooperation):** 24/7 network contact and Mutual Legal Assistance Treaty (MLAT) requests.

---

### SECTION 2: ELECTRONIC EVIDENCE ACQUISITION & INTEGRITY

#### 2.1 Evidence Seizure and Chain of Custody (CoC)
Two evidence items were seized under strict ISO/IEC 27037 protocol:
- **EVD-01 (MSR-605X Hardware Skimmer):** Extracted from Connaught Place ATM Kiosk bezel. Disconnected from power, wrapped in static-neutral bubble wrap, sealed in evidence bag `#CCIC-7781`.
- **EVD-02 (Phantom Smartphone):** Seized in powered-on, unlocked state. Immediately isolated inside a dual-layer RF Faraday Shielding Bag to block remote wipe signals.

#### 2.2 Write-Blocking & Bit-Stream Imaging Protocol
Hardware write-blockers (Tableau T8u USB 3.0 Bridge) were deployed prior to mounting media on forensic workstations. Physical bit-stream image copies were acquired using `dc3dd`.

```
[Target Suspect Device] ──(Read-Only USB)──> [Tableau Hardware Write-Blocker] ──> [Forensic Workstation] ──> SHA-256 Verification
```

#### 2.3 Cryptographic Hash Manifestation (SHA-256)
SHA-256 hash digests were generated immediately post-acquisition and verified prior to forensic examination:

| Item # | Relative File Path | SHA-256 Hash Digest | Integrity Status |
|---|---|---|---|
| EVD-01.1 | `evidence/skimmer_device/msr605_dump.raw` | `0bd8fc1fe19e52b0e3252ff7f39adaae9f4c068bce3db981b8fa9b849117062a` | MATCH / INTACT |
| EVD-01.2 | `evidence/skimmer_device/track2_data.txt` | `b6069b4849181c862053a7f082d1c8164946dbdbfdeee5f2da931f3687992eb0` | MATCH / INTACT |
| EVD-02.1 | `evidence/suspect_phone/chat_backup.json` | `8ff63776610a004a1c86c83ae1cb7d116aa6d29572551651412c805141dcff2d` | MATCH / INTACT |
| EVD-02.2 | `evidence/suspect_phone/gps_logs.csv` | `ba1e81b70ca0565381e58da94625796bd01dc913aff336320ca6a382024955a7` | MATCH / INTACT |
| EVD-02.3 | `evidence/suspect_phone/transaction_history.json` | `5b05f78e5d77f25a4b398894883a53f7d3fc081125b4961f2fe4dd1f8e82f7da` | MATCH / INTACT |
| EVD-02.4 | `evidence/suspect_phone/app_metadata.xml` | `4a3f16d810aba1a5be317853349c6ba79f2ec097d60f2aa66d744b1410b61882` | MATCH / INTACT |
| EVD-02.5 | `cryptography/encrypted_vault.zip` | `24a1a6720a3d13f023f0d3d745427df46431ae2756548e8ceb0c46f97e721e92` | MATCH / INTACT |

---

### SECTION 3: FORENSIC SEARCH & ARTEFACT EXTRACTION FINDINGS

Automated regex analysis (`tools/forensic_search.py`) extracted five critical artefact classes proving crime execution:

1. **Card Credentials & PIN Extraction (`extracted_card_numbers.txt`):**
   - 5 full Track 2 payloads identified (e.g. `4012888899991234=251210123456789`, PIN: `8492`).
2. **Conspiratorial Chat Transcripts (`communication_evidence.csv`):**
   - Direct messages between `@Phantom_Admin` and `Mule_Handler_Delhi` explicitly confirming skimmer placement at Connaught Place HDFC ATM and ₹4.5 Lakh cash conversion to USDT.
3. **Geolocation Mapping (`location_mapping.json`):**
   - GPS logs placing suspect device at Connaught Place ATM Kiosk (lat `28.6315`, lon `77.2167`) at 13:45 UTC on 2026-08-30.
4. **Financial Laundering Audit (`financial_footprint.csv`):**
   - BTC wallet `bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh` (1.482 BTC) and USDT wallet `TR7NHqj...` ($12,500 USDT).
5. **Skimmer Controller Metadata (`app_metadata.xml`):**
   - C2 domain endpoint `https://c2.phantom-swipe-net.cc/api/v1/upload` and BLE MAC address `AA:BB:CC:11:22:33`.

---

### SECTION 4: CRYPTOGRAPHIC ANALYSIS & ETHICAL REFLECTION

#### 4.1 Password Recovery Execution
Target file `cryptography/encrypted_vault.zip` was subjected to a dictionary attack using `tools/password_cracker.py`. The archive was cracked in 0.18 seconds, recovering the password **`phantom2026`**.

Unencrypted file `master_mule_ledger.json` revealed:
- Syndicate Leader: Victor K. (`@Phantom_Admin`)
- Total Cloned Cards: 142 cards
- Total Proceeds: ₹68,500,000 (₹68.5 Lakhs)
- Mule Account details in HDFC and ICICI banks.

#### 4.2 Ethical & Legal Reflection on Decryption
- **Brute-Forcing vs Key Disclosure Orders:** While brute-forcing operates within search warrant parameters without requiring suspect action, key disclosure orders (e.g., Section 69 IT Act) face constitutional scrutiny under **Article 20(3)** of the Indian Constitution (Right against self-incrimination).
- **Password Entropy Deficit:** Despite executing complex financial cybercrimes, the password `phantom2026` exhibited a low effective entropy (\(\approx 18 \text{ bits}\) against dictionary attacks), demonstrating human bias toward memorability over cryptographic strength.

---

### SECTION 5: CROSS-BORDER JURISDICTIONAL CHALLENGES

Investigating cross-border financial cybercrime introduces significant legal and procedural friction:

```
[Indian Law Enforcement] ──(MLAT / 24-48 Months)──> [Foreign Central Authority] ──> [Cloud Service Provider]
[Indian Law Enforcement] ──(Budapest 24/7 Network)─> [Emergency Preservation Request (72 hrs)]
```

1. **Mutual Legal Assistance Treaty (MLAT) Delays:** Standard MLAT processing between India and foreign jurisdictions (e.g. US/EU cloud hosters) requires 12 to 24 months, allowing transient C2 infrastructure to be destroyed.
2. **Cryptocurrency Obfuscation:** CoinJoin mixers and non-compliant offshore exchanges prevent rapid asset freezing.
3. **Data Localization Limits:** Cloud service providers often refuse data production without domestic court orders issued within their parent jurisdiction.

---

### SECTION 6: RECOMMENDATIONS FOR LAW ENFORCEMENT SOP IMPROVEMENTS

1. **Mandatory Faraday First-Responder Kits:** Issue RF-shielding pouches and portable power banks to all field units seizing active mobile evidence.
2. **Automated Cryptographic Hash Auditing:** Integrate automated SHA-256 checkscripts into standard evidence intake workflows.
3. **Adoption of Budapest Convention 24/7 Network Protocols:** Formalize 24/7 point-of-contact channels for emergency data preservation requests to bypass initial MLAT delays.
4. **Chip-and-PIN (EMV) Upgrade Enforcement:** Recommend RBI mandate anti-skimming physical sensors and fallback magnetic stripe suppression on all public ATM kiosks.

---

### AUTHORSHIP & VERIFICATION DECLARATION

I hereby declare that this report represents an objective, forensic technical-legal analysis of the digital evidence seized in Operation Phantom Swipe. All hash values, extracted artefacts, and cracking results have been empirically verified.

**Lead Forensic Examiner:** Parth Bhardwaj (Roll No: 2301730289)  
**Signature:** `Parth Bhardwaj`  
**Date:** September 7, 2026  
**Digital Forensics & Cyber Crime Division, CBI**
