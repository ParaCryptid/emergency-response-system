import os
import subprocess
import sys

def check_gpg_key():
    key_id = "E6B95286AC6227141B449C26D7B417D8E92A829E"
    try:
        output = subprocess.check_output(["gpg", "--list-keys", key_id])
        if key_id in output.decode():
            print("[+] GPG key is present and valid.")
            return True
    except subprocess.CalledProcessError:
        pass
    print("[-] Required GPG key not found or invalid.")
    return False

def unlock_system():
    if check_gpg_key():
        # Replace this with secure decryption commands as needed
        os.system("gpg --batch --yes --decrypt-files ../classified/*.gpg")
        print("[✓] System files unlocked.")
    else:
        print("[-] Unlock failed. GPG key missing or invalid.")
        sys.exit(1)

if __name__ == "__main__":
    print("[*] Running GPG unlock system...")
    unlock_system()
