import cv2
import sounddevice as sd
import numpy as np
import wave
import datetime
import os

def record_video(duration=10, output_folder="../classified"):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("[-] Cannot access camera.")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = 20
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_folder, f"video_{timestamp}.avi")

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    print(f"[*] Recording video to {filename}")
    for _ in range(int(fps * duration)):
        ret, frame = cap.read()
        if ret:
            out.write(frame)

    cap.release()
    out.release()
    print("[✓] Video capture complete.")

def record_audio(duration=10, output_folder="../classified"):
    fs = 44100
    channels = 1
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_folder, f"audio_{timestamp}.wav")

    print(f"[*] Recording audio to {filename}")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=channels, dtype='int16')
    sd.wait()

    with wave.open(filename, 'w') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(audio.tobytes())
    print("[✓] Audio capture complete.")

if __name__ == "__main__":
    print("[*] Running Surveillance Capture Module...")
    os.makedirs("../classified", exist_ok=True)
    record_video(duration=10)
    record_audio(duration=10)
