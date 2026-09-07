import os
import hashlib
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

EVIDENCE_FILES = [
    os.path.join('evidence', 'skimmer_device', 'msr605_dump.raw'),
    os.path.join('evidence', 'skimmer_device', 'track2_data.txt'),
    os.path.join('evidence', 'suspect_phone', 'chat_backup.json'),
    os.path.join('evidence', 'suspect_phone', 'gps_logs.csv'),
    os.path.join('evidence', 'suspect_phone', 'transaction_history.json'),
    os.path.join('evidence', 'suspect_phone', 'app_metadata.xml'),
    os.path.join('cryptography', 'encrypted_vault.zip')
]

MANIFEST_PATH = os.path.join(BASE_DIR, 'chain_of_custody', 'evidence_hashes.sha256')

def calculate_sha256(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(65536):
            sha256.update(chunk)
    return sha256.hexdigest()

def generate_manifest():
    lines = []
    print("Generating SHA-256 Evidence Manifest...")
    for rel_path in EVIDENCE_FILES:
        full_path = os.path.join(BASE_DIR, rel_path)
        if not os.path.exists(full_path):
            print(f"Error: Evidence file missing: {rel_path}")
            sys.exit(1)
        file_hash = calculate_sha256(full_path)
        normalized_path = rel_path.replace('\\', '/')
        lines.append(f"{file_hash}  {normalized_path}")
        print(f"  [+] {file_hash}  {normalized_path}")
    
    with open(MANIFEST_PATH, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines) + '\n')
    print(f"\nManifest successfully saved to: {MANIFEST_PATH}")

def verify_manifest():
    print(f"Verifying SHA-256 Evidence Manifest from: {MANIFEST_PATH}")
    if not os.path.exists(MANIFEST_PATH):
        print(f"Error: Manifest file missing: {MANIFEST_PATH}")
        sys.exit(1)
    
    all_valid = True
    with open(MANIFEST_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(maxsplit=1)
            if len(parts) != 2:
                continue
            expected_hash, rel_path = parts[0], parts[1]
            full_path = os.path.join(BASE_DIR, rel_path.replace('/', os.sep))
            if not os.path.exists(full_path):
                print(f"  [-] MISSING: {rel_path}")
                all_valid = False
                continue
            actual_hash = calculate_sha256(full_path)
            if actual_hash.lower() == expected_hash.lower():
                print(f"  [OK] {rel_path} -> MATCH ({actual_hash[:16]}...)")
            else:
                print(f"  [MISMATCH] {rel_path}\n       Expected: {expected_hash}\n       Actual:   {actual_hash}")
                all_valid = False
    
    if all_valid:
        print("\nSUCCESS: All evidence file SHA-256 hashes match perfectly!")
        return True
    else:
        print("\nFAILURE: Evidence integrity check failed.")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--verify':
        verify_manifest()
    else:
        generate_manifest()
        verify_manifest()
