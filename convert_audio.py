from pydub import AudioSegment

def convert_to_wav(input_path="input.m4a", output_path="input.wav"):
    try:
        print(f"🎧 Converting {input_path} to {output_path}...")
        audio = AudioSegment.from_file(input_path, format="m4a")
        audio.export(output_path, format="wav")
        print("✅ Conversion done.")
    except Exception as e:
        print(f"❌ Conversion failed: {e}")

if __name__ == "__main__":
    convert_to_wav()
