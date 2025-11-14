import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia

import speech_recognition as sr
import wikipedia
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0)

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak something...")
    audio = r.listen(source)

try:
    query = r.recognize_google(audio)
    print("You said:", query)
    summary = wikipedia.summary(query, sentences=1)
    print(summary)
    engine.say(summary)
    engine.runAndWait()
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError:
    print("Speech service error")
except wikipedia.exceptions.DisambiguationError as e:
    print(e.options)
except wikipedia.exceptions.PageError:
    print("Page not found.")



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(text):
    print(f"Bot: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 1000
    recognizer.dynamic_energy_threshold = False

    with sr.Microphone() as source:
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio)
            print(f"You: {query}")
            return query.lower()
        except:
            return None

def chatbot_response(query):
    
    if "hello" in query:
        return "Hello! How can I help you?"
    elif "your name" in query:
        return "I am your assistant."
    elif "open browser" in query or "open google" in query:
        webbrowser.open("https://www.google.com")
        return "Opening browser."
    elif "bye" in query or "exit" in query or "stop" in query:
        return "Goodbye!"
    else:
        return "I didn't understand that."

if __name__ == "__main__":
    speak("Hello. I am your assistant. You can say hello, open browser, or bye.")

    while True:
        query = listen()
        if query:
            response = chatbot_response(query)
            speak(response)
            if "bye" in query or "exit" in query or "stop" in query:
                break