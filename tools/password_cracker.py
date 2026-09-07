import os
import sys
import time

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ZIP_PATH = os.path.join(BASE_DIR, 'cryptography', 'encrypted_vault.zip')
DICT_PATH = os.path.join(BASE_DIR, 'cryptography', 'dictionary.txt')
OUTPUT_DIR = os.path.join(BASE_DIR, 'cryptography', 'decrypted_content')

os.makedirs(OUTPUT_DIR, exist_ok=True)

def simulate_john_hashcat():
    print("==================================================")
    print("OPERATION PHANTOM SWIPE - PASSWORD RECOVERY TOOL")
    print("Mode: Simulated Hashcat / John the Ripper Wordlist Attack")
    print("==================================================")
    print(f"[*] Target Evidence Archive : {ZIP_PATH}")
    print(f"[*] Dictionary Wordlist     : {DICT_PATH}")
    
    # Extract hash format representation (simulating zip2john)
    print("\n[+] Extracting ZIP Hash Format (zip2john output format):")
    zip_hash_str = "$zip2$*0*3*0*6c2a8f90b1...*$/zip2$"
    print(f"    {ZIP_PATH} -> {zip_hash_str[:45]}...")

    if not os.path.exists(ZIP_PATH):
        print(f"[-] Error: Target encrypted file {ZIP_PATH} missing.")
        sys.exit(1)
        
    if not os.path.exists(DICT_PATH):
        print(f"[-] Error: Dictionary file {DICT_PATH} missing.")
        sys.exit(1)
        
    with open(DICT_PATH, 'r', encoding='utf-8') as f:
        passwords = [line.strip() for line in f if line.strip()]

    print(f"\n[*] Loaded {len(passwords)} password candidates into memory.")
    print("[*] Initiating dictionary attack...\n")
    
    cracked_password = None
    start_time = time.time()
    
    # Try pyzipper first, then standard zipfile
    try:
        import pyzipper
        zf = pyzipper.AESZipFile(ZIP_PATH)
    except Exception:
        import zipfile
        zf = zipfile.ZipFile(ZIP_PATH)
        
    attempts = 0
    for pwd in passwords:
        attempts += 1
        pwd_bytes = pwd.encode('utf-8')
        try:
            # Test extracting first file
            first_filename = zf.namelist()[0]
            zf.extract(first_filename, path=OUTPUT_DIR, pwd=pwd_bytes)
            elapsed = time.time() - start_time
            cracked_password = pwd
            print(f"  [ATTEMPT {attempts:02d}] Password: '{pwd}' -> [SUCCESS] CRACKED in {elapsed:.4f} seconds!")
            break
        except Exception:
            print(f"  [ATTEMPT {attempts:02d}] Password: '{pwd}' -> [FAILED] Incorrect password.")
            
    zf.close()
    
    if cracked_password:
        print("\n==================================================")
        print("PASSWORD RECOVERY SUCCESSFUL!")
        print(f"[*] Recovered Password : {cracked_password}")
        print(f"[*] Decrypted Files in : {OUTPUT_DIR}")
        print("==================================================")
        
        extracted_file = os.path.join(OUTPUT_DIR, 'master_mule_ledger.json')
        if os.path.exists(extracted_file):
            print(f"\n[+] Inspecting Decrypted Artefact: {extracted_file}")
            with open(extracted_file, 'r', encoding='utf-8') as f:
                content = f.read()
                print(content[:350] + "\n...")
        return True
    else:
        print("\n[-] Password cracking failed. Wordlist exhausted.")
        sys.exit(1)

if __name__ == '__main__':
    simulate_john_hashcat()
