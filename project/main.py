import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia

# Initialize TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Use default male voice
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
    elif "open instagram" in query or "Instagram" in query:
        webbrowser.open("https://www.instagram.com/")
        return "Opening browser."
    elif "bye" in query or "exit" in query or "stop" in query:
        return "Goodbye!"
    elif "wikipedia" in query:
        try:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "").strip()
            result = wikipedia.summary(query, sentences=2)
            return result
        except wikipedia.exceptions.DisambiguationError:
            return "The topic is too broad. Please be more specific."
        except wikipedia.exceptions.PageError:
            return "I couldn't find anything on that topic."
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
