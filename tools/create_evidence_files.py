import os
import json
import zipfile

BASE_DIR = 'c:/Users/bhard/cyber forensics'

# 1. Skimmer Device Dump (Binary raw file)
msr_dump_path = os.path.join(BASE_DIR, 'evidence/skimmer_device/msr605_dump.raw')
raw_content = bytes([
    0x02, 0x45, 0x52, 0x52, 0x4F, 0x52, 0x03, 0x5F,
    0x25, 0x42, 0x34, 0x30, 0x31, 0x32, 0x38, 0x38, 0x38, 0x38, 0x39, 0x39, 0x39, 0x39, 0x31, 0x32, 0x33, 0x34, 0x5E,
    0x53, 0x48, 0x41, 0x52, 0x4D, 0x41, 0x2F, 0x52, 0x41, 0x4A, 0x45, 0x53, 0x48, 0x5E, 0x32, 0x35, 0x31, 0x32, 0x31,
    0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3F, 0x3B, 0x34, 0x30, 0x31, 0x32, 0x38, 0x38, 0x38,
    0x38, 0x39, 0x39, 0x39, 0x39, 0x31, 0x32, 0x33, 0x34, 0x3D, 0x32, 0x35, 0x31, 0x32, 0x31, 0x30, 0x31, 0x32, 0x33,
    0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3F
])
with open(msr_dump_path, 'wb') as f:
    f.write(raw_content)

# 2. Skimmer Track 2 Data Text
track2_path = os.path.join(BASE_DIR, 'evidence/skimmer_device/track2_data.txt')
track2_content = """# MSR-605X ATM Skimmer Buffer Log - Device ID: SKIM-DEL-9082
# Acquisition Timestamp: 2026-09-02 04:12:00 UTC
# Dump Format: ISO/IEC 7813 Track 2 Magnetic Stripe Data

%B4012888899991234^SHARMA/RAJESH^251210123456789?
;4012888899991234=251210123456789? PIN: 8492
%B5241999988885678^VERMA/AMIT^260810987654321?
;5241999988885678=260810987654321? PIN: 1209
%B4532111122223333^GUPTA/PRIYA^270110456789123?
;4532111122223333=270110456789123? PIN: 4321
%B3712333344445555^MEHTA/VIKRAM^250910789123456?
;3712333344445555=250910789123456? PIN: 9012
%B4916222233334444^SINGH/KARAN^261110321654987?
;4916222233334444=261110321654987? PIN: 5567
"""
with open(track2_path, 'w', encoding='utf-8') as f:
    f.write(track2_content)

# 3. Suspect Phone - Chat Backup JSON
chat_path = os.path.join(BASE_DIR, 'evidence/suspect_phone/chat_backup.json')
chat_data = {
    "application": "Telegram Secure Messaging (Exported Database)",
    "account_owner": "+91-9876501234 (Alias: Phantom_Admin)",
    "chats": [
        {
            "chat_id": "TG-882109",
            "contact": "Mule_Handler_Delhi (+91-9811122233)",
            "messages": [
                {
                    "timestamp": "2026-08-30T14:22:10Z",
                    "sender": "Phantom_Admin",
                    "text": "New skimmer installed at HDFC Kiosk, Connaught Place Block C. BLE device ID is BLE-SKIM-889."
                },
                {
                    "timestamp": "2026-08-30T14:25:00Z",
                    "sender": "Mule_Handler_Delhi",
                    "text": "Copy that. Overlay PIN pad camera battery is fully charged. How many swipes harvested so far?"
                },
                {
                    "timestamp": "2026-08-30T18:40:15Z",
                    "sender": "Phantom_Admin",
                    "text": "Over 45 dumps collected today. I'm encoding blank JCOP Java cards tonight. Use cash withdrawal mules at Karol Bagh ATM at 2:00 AM."
                },
                {
                    "timestamp": "2026-08-31T09:12:44Z",
                    "sender": "Mule_Handler_Delhi",
                    "text": "Cash fetched ₹4,50,000. Converted to USDT address: 0x71C7656EC7ab88b098defB751B7401B5f6d8976F. Vault zip password set to 'phantom2026'."
                }
            ]
        },
        {
            "chat_id": "TG-994122",
            "contact": "Carder_Vendor_Global (@DarkCarderX)",
            "messages": [
                {
                    "timestamp": "2026-09-01T11:05:22Z",
                    "sender": "Phantom_Admin",
                    "text": "Selling fresh Track 1 & Track 2 US/India dumps with 100% valid PINs. Price: $50 per dump in BTC."
                },
                {
                    "timestamp": "2026-09-01T11:10:00Z",
                    "sender": "Carder_Vendor_Global",
                    "text": "Send sample dump for validation."
                },
                {
                    "timestamp": "2026-09-01T11:12:30Z",
                    "sender": "Phantom_Admin",
                    "text": "Sample: 4012888899991234=251210123456789 PIN:8492. Check balance on card."
                }
            ]
        }
    ]
}
with open(chat_path, 'w', encoding='utf-8') as f:
    json.dump(chat_data, f, indent=4)

# 4. Suspect Phone - GPS Logs CSV
gps_path = os.path.join(BASE_DIR, 'evidence/suspect_phone/gps_logs.csv')
gps_content = """timestamp,latitude,longitude,altitude_m,accuracy_m,location_label,connected_wifi
2026-08-30T13:45:00Z,28.6315,77.2167,216.5,4.2,"Connaught Place Block C, New Delhi (ATM Kiosk)","HDFC_ATM_FREE_WIFI"
2026-08-30T14:15:00Z,28.6320,77.2190,217.0,3.8,"Connaught Place Outer Circle, New Delhi","Cafe_Coffee_Day_CP"
2026-08-30T19:30:00Z,28.6508,77.1915,218.2,5.1,"Karol Bagh Metro Station, New Delhi","Airtel_5G_Plus"
2026-08-31T01:45:00Z,28.6520,77.1930,217.8,4.0,"SBI ATM Kiosk, Karol Bagh, New Delhi (Withdrawal Site)","SBI_ATM_Kiosk_Net"
2026-09-01T10:30:00Z,12.9784,77.6408,920.1,3.5,"Indiranagar 100ft Road, Bengaluru (Safehouse)","Phantom_Safehouse_5G"
"""
with open(gps_path, 'w', encoding='utf-8') as f:
    f.write(gps_content)

# 5. Suspect Phone - Transaction History JSON
tx_path = os.path.join(BASE_DIR, 'evidence/suspect_phone/transaction_history.json')
tx_data = {
    "case_reference": "OP-PHANTOM-SWIPE-2026",
    "crypto_wallets": [
        {
            "currency": "Bitcoin (BTC)",
            "address": "bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh",
            "balance_btc": 1.4820,
            "transactions": [
                {
                    "txid": "7f9a8b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a",
                    "type": "RECEIVE",
                    "amount_btc": 0.5000,
                    "timestamp": "2026-09-01T12:00:00Z",
                    "source": "CardersParadise Escrow"
                }
            ]
        },
        {
            "currency": "Tether (USDT - TRC20)",
            "address": "TR7NHqjeKQGJmG4q884U4Z76884U4Z7688",
            "balance_usdt": 12500.00,
            "transactions": [
                {
                    "txid": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
                    "type": "RECEIVE",
                    "amount_usdt": 5500.00,
                    "timestamp": "2026-08-31T09:30:00Z",
                    "source": "Mule_Handler_Delhi"
                }
            ]
        }
    ],
    "online_fraud_purchases": [
        {
            "order_id": "ORD-2026-8891",
            "merchant": "Amazon.in",
            "amount_inr": 89999.00,
            "card_used": "5241999988885678",
            "cardholder_name": "AMIT VERMA",
            "delivery_address": "Flat 402, Indiranagar, Bengaluru, KA - 560038"
        }
    ]
}
with open(tx_path, 'w', encoding='utf-8') as f:
    json.dump(tx_data, f, indent=4)

# 6. Suspect Phone - App Metadata XML
app_xml_path = os.path.join(BASE_DIR, 'evidence/suspect_phone/app_metadata.xml')
app_xml_content = """<?xml version="1.0" encoding="utf-8"?>
<map>
    <string name="app_name">ATM_Ghost_v3.2</string>
    <string name="package_name">com.phantom.skimming.controller</string>
    <string name="ble_target_mac">AA:BB:CC:11:22:33</string>
    <string name="encryption_key_hash">e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855</string>
    <string name="exfiltration_server">https://c2.phantom-swipe-net.cc/api/v1/upload</string>
    <int name="auto_wipe_after_failed_pings" value="5" />
    <boolean name="stealth_mode_enabled" value="true" />
</map>
"""
with open(app_xml_path, 'w', encoding='utf-8') as f:
    f.write(app_xml_content)

# 7. Create Password Protected Vault for Cryptography Component
zip_vault_path = os.path.join(BASE_DIR, 'cryptography/encrypted_vault.zip')
master_ledger = {
    "title": "CONFIDENTIAL CRIMINAL LEDGER - OPERATION PHANTOM SWIPE",
    "syndicate_leader": "Victor K. @Phantom_Admin",
    "total_cloned_cards": 142,
    "total_stolen_funds_inr": 6850000,
    "active_money_mules": [
        {"name": "Ramesh Kumar", "city": "Delhi", "bank": "HDFC", "account_no": "50100234111222"},
        {"name": "Suresh Patel", "city": "Mumbai", "bank": "ICICI", "account_no": "000401556677"}
    ],
    "c2_credentials": {
        "c2_url": "https://c2.phantom-swipe-net.cc/admin",
        "username": "phantom_root",
        "password_hash": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQOEg6Lruj3vjPGga31lW"
    }
}

temp_json_path = os.path.join(BASE_DIR, 'cryptography/master_mule_ledger.json')
with open(temp_json_path, 'w', encoding='utf-8') as f:
    json.dump(master_ledger, f, indent=4)

# Create zip with password 'phantom2026'
try:
    import pyzipper
    with pyzipper.AESZipFile(zip_vault_path, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(b"phantom2026")
        zf.write(temp_json_path, arcname="master_mule_ledger.json")
    print("Created AES encrypted zip with pyzipper successfully.")
except Exception as e:
    print(f"Fallback zip creation error: {e}")

# Clean up unencrypted master_mule_ledger.json until cracked
if os.path.exists(temp_json_path):
    os.remove(temp_json_path)

# 8. Create dictionary wordlist for Cracking
dict_path = os.path.join(BASE_DIR, 'cryptography/dictionary.txt')
words = [
    "admin", "password", "123456", "secret", "phantom", "cyber2026",
    "phantom2026", "skimmer123", "carder2026", "operator", "vault123"
]
with open(dict_path, 'w', encoding='utf-8') as f:
    f.write("\n".join(words))

print("All synthetic evidence files successfully generated.")
