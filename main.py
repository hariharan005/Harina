#!/usr/bin/env python3

from gtts import gTTS
import speech_recognition as sr
import pyttsx3
import os

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
        audio = recognizer.listen(source, timeout=5)  # Timeout after 5 seconds of silence

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

def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save('out.mp3')
    # Play the generated audio file (Linux command, adjust for your system)
    os.system("play out.mp3")

if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I assist you today?")
    
    while True:
        command = listen()
        
        if "stop" in command:
            speak("Goodbye!")
            break
        elif "your_name" in command:
            speak("I am Jarvis, your virtual assistant.")
        elif command:
            speak("I'm sorry, I didn't understand that command. Please try again.")
