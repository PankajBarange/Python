import speech_recognition as sr
import pyttsx3
import wikipedia

# Initialize TTS engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
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
        except:
            return None

def chatbot_response(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError:
        return "The topic is too broad. Please be more specific."
    except wikipedia.exceptions.PageError:
        return "I couldn't find anything on that topic."
    except:
        return "Sorry, I couldn't fetch information."

if __name__ == "__main__":
    speak("Hello. Ask me anything and I will tell you from Wikipedia.")

    while True:
        query = listen()
        if query:
            if "bye" in query or "exit" in query or "stop" in query:
                speak("Goodbye!")
                break
            response = chatbot_response(query)
            speak(response)