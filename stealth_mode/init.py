import os
import time
import shutil

# Stealth wipe function
def wipe_classified_data(target_folder="../classified"):
    print("[!] Stealth Wipe Activated!")
    for root, dirs, files in os.walk(target_folder, topdown=False):
        for name in files:
            try:
                file_path = os.path.join(root, name)
                with open(file_path, "ba+") as f:
                    length = f.tell()
                    f.seek(0)
                    f.write(b"\x00" * length)
                os.remove(file_path)
                print(f"[x] Shredded: {file_path}")
            except Exception as e:
                print(f"[!] Failed to wipe {file_path}: {e}")
    for name in dirs:
        dir_path = os.path.join(root, name)
        try:
            shutil.rmtree(dir_path)
        except:
            pass
    print("[✓] Classified data wiped.")

# Dummy decoy interface
def launch_decoy():
    print("""
***************
*  DASHBOARD  *
*  STATUS OK  *
***************
> All systems normal.
> No threats detected.
> Uptime: 300d 14h
""")

if __name__ == "__main__":
    print("[*] Running Stealth Mode...")
    # Simulate condition trigger (invalid login attempt)
    trigger_stealth = True  # Change this to logic hook
    if trigger_stealth:
        launch_decoy()
        time.sleep(2)
        wipe_classified_data()
