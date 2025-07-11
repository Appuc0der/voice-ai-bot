import speech_recognition as sr
from gtts import gTTS
import base64
import io

from llm import ask_groq
def speak_text(text):
    tts = gTTS(text)
    with io.BytesIO() as audio_bytes:
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        b64 = base64.b64encode(audio_bytes.read()).decode()
        audio_html = f'<audio autoplay controls><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
        st.markdown(audio_html, unsafe_allow_html=True)


    print("📝 Transcribing...")
    try:
        text = recognizer.recognize_google(audio)
        print(f"❓ You said: {text}")
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand the audio."
    except sr.RequestError:
        return "Speech recognition service is unavailable."

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    prompt = transcribe()
    print("🤖 Getting response from LLM...")
    response = ask_groq(prompt)
    print(f"💬 Bot says: {response}")
    print("🔊 Speaking...")
    speak(response)
