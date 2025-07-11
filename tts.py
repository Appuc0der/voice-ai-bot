import pyttsx3

def speak_text(text):
    print("🔊 Speaking...")
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)   # You can adjust speed here
    engine.setProperty('volume', 1.0) # Max volume
    engine.say(text)
    engine.runAndWait()
