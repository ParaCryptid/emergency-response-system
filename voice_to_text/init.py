import whisper
import os
import datetime

def transcribe_audio(audio_path, output_folder="../classified"):
    model = whisper.load_model("base")
    print(f"[*] Transcribing: {audio_path}")
    result = model.transcribe(audio_path)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    transcript_path = os.path.join(output_folder, f"transcript_{timestamp}.txt")
    with open(transcript_path, "w") as f:
        f.write(result["text"])
    print(f"[✓] Transcription complete: {transcript_path}")

if __name__ == "__main__":
    print("[*] Running Voice-to-Text Module...")
    os.makedirs("../classified", exist_ok=True)
    # Auto-find latest WAV file
    files = [f for f in os.listdir("../classified") if f.endswith(".wav")]
    if not files:
        print("[-] No audio files found to transcribe.")
    else:
        latest_audio = sorted(files)[-1]
        transcribe_audio(os.path.join("../classified", latest_audio))
