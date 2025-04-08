import os

def show_package_plan():
    print("[*] Packaging Plan:")
    print(" - Debian (.deb): ./ci_cd/build_deb.sh")
    print(" - Windows (.exe): ./ci_cd/build_exe.bat")
    print(" - Linux Portable (.AppImage): ./ci_cd/build_appimage.sh")
    print(" - macOS (.pkg): ./ci_cd/build_pkg.sh")
    print(" - Bootable ISO (.iso): ./ci_cd/build_iso.sh")

    print("\n[✓] Build scripts are staged for all OS targets.")
    print("NOTE: Ensure proper signing and architecture for each target system.")

if __name__ == "__main__":
    print("[*] Running Package Build Overview...")
    show_package_plan()
