#!/usr/bin/env python3

import pyttsx3
#import speech_recognition as sr

#Initialize the TTS engine
engine = pyttsx3.init()

# Set properties 
engine.setProperty('rate', 140) # Speed of speech

# My AI start to speech
text_speak = "Hello, How can i assist you today!"

# Convert and speak the text
engine.say(text_speak)

# Wait for the speech to finish
engine.runAndWait()
