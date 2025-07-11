import speech_recognition as sr
import pyttsx3
from llm import ask_groq

def transcribe():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening... Please speak clearly.")
        audio = recognizer.listen(source)

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
