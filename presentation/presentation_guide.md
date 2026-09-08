# PRESENTATION & VIVA VOCE GUIDE
## OPERATION PHANTOM SWIPE: CROSS-BORDER ATM & CREDIT CARD FRAUD RING

**Course Code & Title:** ENSP303 - Cyber Crime Investigation & Digital Forensics (Unit 1)  
**Student Name:** Parth Bhardwaj  
**Roll Number:** 2301730289  
**Institution:** School of Engineering & Technology, K.R. Mangalam University, Gurugram  
**GitHub Repository:** [bhardwajparth51/Cyber-Crime-Investigation-And-Digital-Forensics-Lab-Assignment-1](https://github.com/bhardwajparth51/Cyber-Crime-Investigation-And-Digital-Forensics-Lab-Assignment-1)  

---

## 🎯 1. EXECUTIVE PRESENTATION SLIDE OUTLINE

### Slide 1: Title & Student Credentials
- **Title:** Operation Phantom Swipe: Investigating a Cross-Border ATM & Credit Card Fraud Ring
- **Presenter:** Parth Bhardwaj (Roll No: 2301730289)
- **Course:** ENSP303 - Unit 1: Foundations of Digital Forensics
- **Case Reference:** `DFS-2026-OPSW-009`

### Slide 2: Case Overview & Investigation Objectives
- **Scenario:** High-frequency ATM Track 2 skimming and online credit card fraud detected across New Delhi and Bengaluru.
- **Seized Media:**
  1. **EVD-01:** MSR-605X Magnetic Stripe Reader/Writer Hardware Skimmer PCB & PIN Pad Camera Overlay.
  2. **EVD-02:** OnePlus 11 5G Smartphone (Suspect Victor K. `@Phantom_Admin`).
- **Core Objectives:** Cybercrime taxonomy mapping, evidence collection simulation, forensic string/regex analysis, password cracking, legal-technical reporting, and CI workflow validation.

### Slide 3: Cybercrime Taxonomy & Statutory Legal Mapping
- **Observed Crimes:** ATM Skimming, Card Cloning, Identity Theft, Wire Fraud, C2 Exfiltration, Crypto Money Laundering.
- **Indian IT Act (2000/2008):** Sec 43 (Unauthorized Access), Sec 66 (Hacking), Sec 66C (Identity Theft), Sec 66D (Cheating by Personation), Sec 66E (Privacy Violation).
- **IPC 1860 / BNS 2023:** Sec 419/319 (Personation), Sec 420/318 (Cheating), Sec 468/336 (Forgery), Sec 471/340 (Using Forged Record), Sec 120B/61 (Conspiracy).
- **Budapest Convention:** Articles 2 (Illegal Access), 3 (Illegal Interception), 6 (Device Misuse), 14–21 (Procedural Law), 23–35 (International MLA).
- **Landmark Supreme Court Judgments:**
  - *Anvar P.V. v. P.K. Basheer (2014):* Section 65B mandatory requirement.
  - *Arjun Panditrao Khotkar v. Kailash Kushanrao Gorantyal (2020):* Reaffirmed 65B(4) certificate requirement when original device cannot be brought to court.
  - *Selvi v. State of Karnataka (2010):* Protection against involuntary scientific tests under Article 20(3).
  - *P. Gopalakrishnan @ Dileep v. State of Kerala (2020):* Cloned copy of memory card/pen drive as document for defence.

### Slide 4: Electronic Evidence Collection & Chain of Custody
- **Write-Blocker Protocol:** Tableau T8u USB 3.0 Hardware Bridge preventing disk write operations.
- **RF Faraday Shielding:** Dual-layer Faraday isolation bag protecting active mobile device from remote wipe commands.
- **Order of Volatility:** RAM & active BLE connections captured prior to power-off.
- **SHA-256 Hashes:** 7 evidence files hashed and verified post-acquisition (`evidence_hashes.sha256`).

### Slide 5: Forensic Search & Artefact Extraction Engine
- **Engine:** Python regex string search parser ([`forensic_search.py`](file:///c:/Users/bhard/cyber%20forensics/tools/forensic_search.py)).
- **5 Extracted Artefact Classes:**
  1. `extracted_card_numbers.txt`: 6 Track 2 card dumps with cleartext PINs (`4012888899991234`, PIN: `8492`).
  2. `communication_evidence.csv`: Telegram chat transcripts between `@Phantom_Admin` and money mules.
  3. `location_mapping.json`: GPS logs placing suspect at Connaught Place & Karol Bagh ATM Kiosks.
  4. `financial_footprint.csv`: BTC (`bc1q...`) & USDT (`TR7N...`) wallets + Amazon delivery addresses.
  5. `evidence_log.md`: Forensic search strategy and evidence inventory audit trail.

### Slide 6: Cryptography & Password Recovery Simulation
- **Target Vault:** `cryptography/encrypted_vault.zip`
- **Cracking Engine:** Python dictionary attack script ([`password_cracker.py`](file:///c:/Users/bhard/cyber%20forensics/tools/password_cracker.py)) simulating Hashcat Mode 13600 / `zip2john`.
- **Result:** Recovered password **`phantom2026`** in 0.13s and unlocked [`master_mule_ledger.json`](file:///c:/Users/bhard/cyber%20forensics/cryptography/decrypted_content/master_mule_ledger.json).
- **Ethical Reflection:** Brute-forcing under search warrant vs Key Disclosure Orders under Article 20(3) of Constitution of India (Right against self-incrimination). Entropy analysis showing `phantom2026` effective entropy drops to \(\approx 18 \text{ bits}\) against wordlist attacks.

### Slide 7: Cross-Border Challenges & Law Enforcement Recommendations
- **MLAT Delays:** 12–24 month friction in obtaining cloud host logs from foreign jurisdictions.
- **Crypto Obfuscation:** P2P mule networks and offshore exchanges.
- **SOP Recommendations:**
  1. Mandatory Faraday First-Responder kits.
  2. Automated SHA-256 hash validation pipelines.
  3. Budapest 24/7 point-of-contact network protocols for emergency 72-hour preservation requests.
  4. RBI mandatory Chip-and-PIN (EMV) hardware sensor enforcement on ATM kiosks.

### Slide 8: GitHub CI Compliance & Repository Architecture
- **GitHub Repository:** Fully structured with `.gitignore`, `README.md`, `screenshots/`, `tools/`, `chain_of_custody/`, `evidence/`, `extracted_artefacts/`, `cryptography/`, and `legal_technical_report/`.
- **Automated CI:** GitHub Actions workflow ([`.github/workflows/validate.yml`](file:///c:/Users/bhard/cyber%20forensics/.github/workflows/validate.yml)) automatically testing evidence hashes, search scripts, cracking engine, and report generation.

---

## 💻 2. LIVE DEMONSTRATION SCRIPT FOR PROFESSOR

During your viva presentation, open your PowerShell terminal in `c:\Users\bhard\cyber forensics` and run these 4 commands step-by-step:

### Step 1: Demonstrate SHA-256 Cryptographic Hash Verification
```powershell
python tools/hash_generator.py --verify
```
*Say to Professor:*  
> "First, I will demonstrate evidence integrity verification under ISO 27037 standards. Our python tool checks all 7 seized evidence files against the original SHA-256 hash manifest. As shown, all 7 files match 100% with zero tampering."

### Step 2: Demonstrate Automated Forensic Artefact Extraction Engine
```powershell
python tools/forensic_search.py
```
*Say to Professor:*  
> "Next, I run our automated forensic search engine. It parses the raw MSR-605X skimmer dump, chat backups, and GPS logs using regular expressions. It extracts 5 distinct artefact classes into structured CSV, JSON, and text deliverables, including Track 2 payment card payloads, cleartext PINs, conspiratorial chat logs, and ATM kiosk GPS coordinates."

### Step 3: Demonstrate Password Recovery Cracking Simulation
```powershell
python tools/password_cracker.py
```
*Say to Professor:*  
> "Now I will demonstrate the cryptography component. The suspect stored a confidential master ledger inside an encrypted zip archive. Our tool extracts the zip header hash and executes a wordlist dictionary attack. It recovers the password 'phantom2026' in 0.13 seconds and decrypts the master mule ledger revealing ₹68.5 Lakhs in stolen funds."

### Step 4: Demonstrate Legal Report & CI Workflow Compliance
```powershell
python tools/generate_report.py
```
*Say to Professor:*  
> "Finally, our report generator compiles the 4–6 page legal-technical report into styled PDF and DOCX formats. Furthermore, our repository includes a GitHub Actions workflow that automatically validates all deliverables and hash manifests on every push."

---

## ❓ 3. TOP VIVA VOCE QUESTIONS & HIGH-SCORING ANSWERS

### Q1: What is Section 65B of the Indian Evidence Act / Section 63 of BSA 2023, and why is it mandatory?
**Answer:**  
"Section 65B of the Indian Evidence Act (now Section 63 of Bharatiya Sakshya Adhiniyam, 2023) lays down the special procedure for the admissibility of electronic records in court. Under the landmark Supreme Court rulings in *Anvar P.V. v. P.K. Basheer (2014)* and *Arjun Panditrao Khotkar v. Kailash Kushanrao Gorantyal (2020)*, producing a Section 65B(4) certificate is a mandatory condition precedent for admitting secondary electronic records (such as printouts, disk images, or extracted chat logs) whenever the original physical device cannot be produced in court."

### Q2: Why did you use SHA-256 instead of MD5 or SHA-1 for evidence hashing?
**Answer:**  
"MD5 and SHA-1 are cryptographically broken due to practical collision attacks (e.g., Flame malware, SHAttered attack). NIST SP 800-86 and ISO 27037 mandate SHA-256 (or SHA-512) because SHA-256 offers 256-bit preimage resistance and collision resistance, ensuring that no two distinct digital evidence files can produce the same hash digest."

### Q3: What is the Order of Volatility, and how did you handle the suspect mobile phone?
**Answer:**  
"The Order of Volatility dictates that the most ephemeral data must be collected first: RAM and network registers -> swap space -> hard disk -> archived media. For the active suspect smartphone (EVD-02), we immediately isolated it inside a dual-layer RF Faraday Shielding Bag to prevent remote cloud wipes (Google/Apple Find My), connected a portable battery pack to maintain power, and captured volatile RAM/BLE connections before executing a write-blocked physical acquisition."

### Q4: What is the legal/ethical difference between brute-forcing encryption and issuing a Lawful Key Disclosure Order?
**Answer:**  
"Brute-forcing operates under a lawful search warrant without requiring active suspect participation, preserving the suspect's constitutional protection against self-incrimination under Article 20(3) of the Indian Constitution (*Selvi v. State of Karnataka*). In contrast, a statutory Key Disclosure Order (e.g., Section 69 IT Act 2000) compels the suspect to disclose passphrases, which can face constitutional challenges regarding self-incrimination unless restricted to hardware access."

### Q5: Why was password 'phantom2026' cracked so quickly despite having 11 characters?
**Answer:**  
"Although `phantom2026` is 11 characters long with a theoretical entropy of 56.8 bits, its effective entropy against a targeted dictionary attack is only \(\approx 18 \text{ bits}\). Because cybercriminals combine common words (`phantom`) with predictable numbers (`2026`), wordlist and rule-based attacks (like Hashcat/John the Ripper) easily bypass brute-force complexity, demonstrating human bias toward operational convenience over security."
