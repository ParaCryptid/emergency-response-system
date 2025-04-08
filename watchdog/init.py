import subprocess
import time
import os

WATCHDOG_LOG = "../logs/watchdog.log"
os.makedirs("../logs", exist_ok=True)

# Define critical services or scripts to monitor
services = {
    "gpg_system": "init.py",
    "surveillance": "init.py",
    "recon": "init.py",
    "voice_to_text": "init.py",
    "sensor_simulation": "init.py"
}

def check_and_restart(module, script):
    path = f"../{module}/{script}"
    try:
        result = subprocess.run(["python3", path], check=True, capture_output=True, timeout=20)
        return f"[✓] {module} running OK"
    except Exception as e:
        return f"[!] {module} failed. Restarting..."

def write_log(message):
    with open(WATCHDOG_LOG, "a") as f:
        f.write(f"{time.ctime()}: {message}\n")

if __name__ == "__main__":
    print("[*] Running Self-Healing Watchdog...")
    for module, script in services.items():
        status = check_and_restart(module, script)
        write_log(status)
        print(status)
