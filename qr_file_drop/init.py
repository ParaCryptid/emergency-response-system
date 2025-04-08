import os
import qrcode
import datetime

def generate_qr_from_file(filepath, output_folder="../classified"):
    if not os.path.exists(filepath):
        print(f"[-] File not found: {filepath}")
        return

    with open(filepath, "r") as f:
        content = f.read()

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(content)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    img_path = os.path.join(output_folder, f"qrfile_{timestamp}.png")
    img.save(img_path)
    print(f"[✓] QR code saved: {img_path}")

if __name__ == "__main__":
    print("[*] Running QR File Drop Module...")
    os.makedirs("../classified", exist_ok=True)
    sample_txt = "../classified/sample_to_encode.txt"

    if not os.path.exists(sample_txt):
        with open(sample_txt, "w") as f:
            f.write("Secure sample data drop - encoded via QR.")
    generate_qr_from_file(sample_txt)
