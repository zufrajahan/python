import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()  # Run the speech synthesis

def input_instruction():
    try:
        with aa.Microphone() as origin:
            print("Listening...")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', "").strip()
                print("Recognized:", instruction)
                return instruction
    except:
        return ""  # Return empty string if no instruction is detected

def play_jarvis():
    while True:  # Keep listening for commands
        instruction = input_instruction()
        if instruction:  # Only process if instruction is not empty
            if "play" in instruction:
                song = instruction.replace("play", "").strip()
                talk("Playing " + song)
                pywhatkit.playonyt(song)

            elif "time" in instruction:
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk("Current time is " + time)

            elif "date" in instruction:
                date = datetime.datetime.now().strftime("%d /%m /%Y")
                talk("Today's date is " + date)

            elif "how are you" in instruction:
                talk("I am fine. What about you?")

            elif "what is your name" in instruction:
                talk("I am Jarvis, your assistant.")

            elif "who is" in instruction:
                human = instruction.replace('who is', "").strip()
                info = wikipedia.summary(human, 1)
                print(info)
                talk(info)

            else:
                talk("Please repeat.")

play_jarvis()
