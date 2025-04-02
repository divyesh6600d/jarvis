import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Listening...")
    audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        speak(f"You said: {command}")
    except Exception as e:
        print("Could not understand the audio.")
        speak("Could not understand the audio.")

