#!/usr/bin/env python3

from gtts import gTTS
import speech_recognition as sr
import os
import wikipedia
import datetime


hour = int(datetime.datetime.now().hour)

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout='')  # Timeout after 5 seconds of silence

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand. Please try again.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(f"Wikipedia says: {result}")
    except wikipedia.exceptions.DisambiguationError as e:
        speak("Multiple results found. Please be more specific.")
    except wikipedia.exceptions.PageError as e:
        speak("No results found. please try again.")

def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save('out.mp3')
    # Play the generated audio file (Linux command, adjust for your system)
    os.system("play -q out.mp3")

if __name__ == "__main__":
    speak("Hello, How can I assist you today?")
    
    while True:
        command = listen()
        
        if "stop" in command or "bye" in command:
            speak("You are welcome, i am here to help you !")
            break
        
        elif "good morning" in command or "morning" in command:
            if hour>= 0 and hour<12:
                speak("Good morning")
            elif hour>= 12 and hour<18:
                speak("good afternoon")
            else:
                speak("good evening")
                
        elif "your name" in command or "name" in command or "call you" in command:
            speak("I am Harina, your virtual assistant.")
        elif "search" in command or "what is" in command or "who is":
            search_query = command.replace("search", "")
            search_wikipedia(search_query)
        elif command:
            speak("I'm sorry, I didn't understand that command. Please try again.")
