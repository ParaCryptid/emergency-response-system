import os

def get_user_role():
    role_file = "../role.txt"
    if not os.path.exists(role_file):
        print("[!] No role assigned. Defaulting to AGENT.")
        return "AGENT"
    with open(role_file, "r") as f:
        role = f.read().strip().upper()
    if role not in ["AGENT", "ADMIN"]:
        print("[!] Invalid role in file. Defaulting to AGENT.")
        return "AGENT"
    print(f"[✓] Role detected: {role}")
    return role

def launch_interface(role):
    if role == "ADMIN":
        print("[*] Launching Admin dashboard tools...")
        # Insert admin-specific features
    else:
        print("[*] Launching Agent interface...")
        # Insert limited feature set

if __name__ == "__main__":
    print("[*] Running Role Access Module...")
    role = get_user_role()
    launch_interface(role)
