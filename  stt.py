import speech_recognition as sr

def transcribe_audio_file(filepath="voice.wav"):
    recognizer = sr.Recognizer()

    with sr.AudioFile(filepath) as source:
        print("📂 Reading audio file...")
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"📝 Transcribed: {text}")
        return text
    except sr.UnknownValueError:
        print("😕 Could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"❌ STT error: {e}")
        return None
