from gtts import gTTS
import os

def speak_text_streamlit(text, filename="output.mp3"):
    try:
        tts = gTTS(text)
        tts.save(filename)
        return filename
    except Exception as e:
        print(f"Text-to-speech failed: {e}")
        return None
