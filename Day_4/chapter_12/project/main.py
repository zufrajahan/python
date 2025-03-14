import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "dc821e5fc55145159ded305c7e38d222"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()  # Convert to JSON
        articles = data["articles"]  # Get news articles

        for article in articles:  
            speak(article["title"])  # Print headline
            
    else:
        # let openAI handle the request
        pass

if __name__ == "__main__":
    speak("Initializing Jarvis.... ")
    while True:
        # listen for the wake word jarvis
        # obtain audio from  micrphone
        r = sr.Recognizer()
       

        print("Recongnizing")
        try:
            with sr.Microphone() as source:
                print("Listening...!")
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("ya")
                # listen for command
                with sr.Microphone() as source:
                    print("jarvis Active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print("Error ; {0}".format(e))    