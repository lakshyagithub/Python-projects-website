# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 19:48:12 2023

@author: laksh
"""

import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speech_by_us():
    engine.say("How can I help you? Suggested: How to open a door?")
    print("How can I help you? Suggested: How to open a door?")
    speech_by_you = sr.Recognizer()
    with sr.Microphone() as source:
        audio=speech_by_you.listen(source)
        voice_data = ''
        try:
            voice_data = speech_by_you.recognize_google(audio, language="en-in")
        except sr.UnknownValueError:
            #Speech by computer
            engine.say("Can you please shout what you just said so that I can hear it.")
            print("Can you please shout what you just said so that I can hear it.")
        print(voice_data)
        if voice_data == "time please":
            engine.say("How to view time: Step 1: Walk to the room in which you have the clock. Step 2: Face towards the clock. Step 3: View the time.")
            print("How to view time: Step 1: Walk to the room in which you have the clock. Step 2: Face towards the clock. Step 3: View the time.")
        elif voice_data == "name":
            engine.say("My file name is my name.")
            print("My file name is my name.")
        elif voice_data == "how to open a door":
            engine.say("Just push it. Done!")
            print("Just push it. Done!")

speech_by_us()
engine.runAndWait()