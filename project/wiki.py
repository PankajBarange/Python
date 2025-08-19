import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia

engine = pyttsx3.init()
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now...")
    audio = recognizer.listen(source)

try:
    query = recognizer.recognize_google(audio)
    summary = wikipedia.summary(query, sentences=4)
    print(summary)
    engine.say(summary)
    engine.runAndWait()
except:
    engine.say("Sorry, I could not find information.")
    engine.runAndWait()


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use default male voice
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
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            query = recognizer.recognize_google(audio)
            print(f"You: {query}")
            return query.lower()
        except sr.WaitTimeoutError:
            speak("I didn't hear anything. Please try again.")
            return None
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand.")
            return None
        except sr.RequestError:
            speak("Network error. Please check your internet.")
            return None

def chatbot_response(query):
    if "hello" in query:    
        return "Hello! How can I help you?"
    elif "your name" in query:
        return "I am your assistant."
    elif "open browser" in query or "open google" in query:
        webbrowser.open("https://www.google.com")
        return "Opening Google."
    elif "open instagram" in query:
        webbrowser.open("https://www.instagram.com/")
        return "Opening Instagram."
    elif "bye" in query or "exit" in query or "stop" in query:
        return "Goodbye!"
    else:
        return "I didn't understand that."

if __name__ == "__main__":
    speak("Hello. I am your assistant. You can ask anything.")

    while True:
        query = listen()
        if query:
            response = chatbot_response(query)
            speak(response)
            if "bye" in query or "exit" in query or "stop" in query:
                break
