# ELECTRONIC EVIDENCE HANDLING & ACQUISITION STANDARD OPERATING PROCEDURE (SOP)
**Document Reference:** CCIC-SOP-EVD-2026-01  
**Applicable Standards:** ISO/IEC 27037:2012 (Guidelines for identification, collection, acquisition, and preservation of digital evidence), NIST SP 800-86 (Guide to Integrating Forensic Techniques into Incident Response), Section 65B of Indian Evidence Act / Section 63 of Bharatiya Sakshya Adhiniyam (BSA 2023).

---

## 1. PRINCIPLES OF DIGITAL EVIDENCE HANDLING

1. **Principle of Non-Contamination (Order of Volatility):**
   No action taken by law enforcement or forensic examiners shall alter data subsequently relied upon in court. Volatile memory (RAM, active BLE connections, network sockets) must be acquired prior to powered device shutdown.

2. **Auditability and Repeatability:**
   All acquisition procedures, hardware models, write-blocker firmware versions, and command sequences must be logged in real-time such that an independent forensic examiner can replicate the process and arrive at identical SHA-256 hash digests.

3. **Chain of Custody Continuity:**
   Every transfer of physical or digital evidence must document the date, time, identity of transferor/transferee, reason for transfer, and cryptographic verification status.

---

## 2. HARDWARE AND SOFTWARE WRITE-BLOCKING MECHANISMS

### A. Hardware Write-Blockers
- **Device Used:** Tableau T8u Forensic USB 3.0 Bridge & WiebeTech UltraDock v5.
- **Functionality:** Intercepts all write commands (`WRITE (10)`, `WRITE (16)`, `FORMAT`, `FLUSH CACHE`) sent from the host operating system at the controller logic level. Only read commands (`READ (10)`, `READ INQUIRY`) are passed to the target storage media.
- **Verification:** Before connecting suspect media, host workstations run write-blocker validation tests by issuing write operations to a test flash drive and confirming hardware-level rejection (`STATUS_WRITE_PROTECTED`).

### B. Software Write-Blocking & OS Enforcement
- **Linux/Unix Forensic Workstations:** Storage devices mounted using read-only flags:
  ```bash
  mount -o ro,loop,noexec /dev/sdb1 /mnt/forensic_target
  ```
- **Windows Registry Enforcement:**
  `HKLM\SYSTEM\CurrentControlSet\Control\StorageDevicePolicies\WriteProtect = 1`

---

## 3. PHYSICAL ISOLATION & FARADAY PROTOCOLS

For **EVD-02 (Phantom Smartphone)**:
1. **Radio Frequency (RF) Shielding:** Device immediately placed in a dual-layer Faraday Shielding Enclosure Bag (attenuation > 90 dB across 700 MHz - 6 GHz) to block cellular (GSM/LTE/5G), Wi-Fi, Bluetooth, and GPS signals.
2. **Anti-Remote Wipe Safeguard:** RF isolation prevents suspects from issuing remote wipe commands via cloud device management portals (e.g., Apple Find My or Google Find My Device).
3. **Flight Mode & Power Management:** Device maintained in RF-isolated enclosure while connected to external battery power packs to prevent shutdown battery exhaustion during transport.

---

## 4. BIT-STREAM IMAGING & HASH MANIFESTATION

1. **Bit-Stream Acquisition:**
   - Raw bit-for-bit physical image captured using `dc3dd` / `FTK Imager`:
     ```bash
     dc3dd if=/dev/sdb hash=sha256 log=acquisition.log of=/forensics/EVD01_image.raw
     ```
2. **Cryptographic Hashing (SHA-256):**
   - Dual SHA-256 hashing executed during bit-stream transfer (Read-Hash vs Write-Hash).
   - If `Read-Hash != Write-Hash`, the acquisition is immediately aborted and hardware connectors inspected for bus errors.

---

## 5. ADMISSIBILITY UNDER INDIAN LAW (BSA 2023 / IT ACT 2000)

Under **Section 63 of Bharatiya Sakshya Adhiniyam, 2023** (formerly Section 65B of Indian Evidence Act, 1872):
- Digital evidence must be accompanied by an **Electronic Evidence Certificate** signed by the person in charge of the computer system / forensic laboratory.
- The certificate confirms:
  1. Operating status of computer/device during evidence extraction.
  2. Non-tampering of source media via verified SHA-256 cryptographic hashes.
  3. Integrity of write-blocked imaging environment.
