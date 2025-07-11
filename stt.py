import speech_recognition as sr

def transcribe_audio_file(filepath="input.wav"):
    recognizer = sr.Recognizer()

    try:
        with sr.AudioFile(filepath) as source:
            print("🎙️ Reading audio file...")
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        print("📝 Transcribed:", text)
        return text
    except FileNotFoundError:
        print("❌ input.wav not found.")
    except sr.UnknownValueError:
        print("❓ Could not understand the audio.")
    except Exception as e:
        print(f"⚠️ Error: {e}")
