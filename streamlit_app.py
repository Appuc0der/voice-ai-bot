import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
import os
import requests

st.title("🎙️ Voice AI Assistant")

# Helper: Convert uploaded .m4a or .wav to WAV
def convert_to_wav(uploaded_file):
    if uploaded_file.name.endswith(".m4a"):
        audio = AudioSegment.from_file(uploaded_file, format="m4a")
    elif uploaded_file.name.endswith(".wav"):
        audio = AudioSegment.from_file(uploaded_file, format="wav")
    else:
        st.error("Unsupported file format.")
        return None
    wav_path = "input.wav"
    audio.export(wav_path, format="wav")
    return wav_path

# Helper: Transcribe audio using speech_recognition
def transcribe(wav_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "❌ Could not understand audio"
    except sr.RequestError:
        return "❌ Speech Recognition service unavailable"

# Helper: Ask Groq LLM
def ask_groq(prompt):
    api_key = st.secrets["GROQ_API_KEY"]
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mixtral-8x7b-32768",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()["choices"][0]["message"]["content"]

# File Upload UI
uploaded_file = st.file_uploader("📁 Upload .wav or .m4a file", type=["wav", "m4a"])
if uploaded_file:
    st.audio(uploaded_file)
    wav_path = convert_to_wav(uploaded_file)
    if wav_path:
        st.write("📝 Transcribing...")
        prompt = transcribe(wav_path)
        st.success(f"You said: **{prompt}**")

        st.write("🤖 Asking LLM...")
        reply = ask_groq(prompt)
        st.info(f"💬 AI says: **{reply}**")

        # Optional TTS
        tts = gTTS(reply)
        tts.save("response.mp3")
        st.audio("response.mp3", format="audio/mp3")
