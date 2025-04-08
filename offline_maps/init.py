import webbrowser
import os

def launch_map():
    map_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "map.html"))
    if os.path.exists(map_file):
        print(f"[*] Opening offline map: {map_file}")
        webbrowser.open(f"file://{map_file}")
    else:
        print("[-] map.html not found. Please add your offline map tile interface.")

if __name__ == "__main__":
    print("[*] Running Offline Map Module...")
    launch_map()
