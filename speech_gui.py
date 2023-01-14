# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 18:19:31 2023

@author: laksh
"""

from tkinter import *
import speech_recognition as sr
import pyttsx3

root = Tk()
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
            speak("Can you please shout what you just said so that I can hear it.")
            print("Can you please shout what you just said so that I can hear it.")
        print(voice_data)
        if "time" in voice_data:
            speak("How to view time: Step 1: Walk to the room in which you have the clock. Step 2: Face towards the clock. Step 3: View the time.")
            print("How to view time: Step 1: Walk to the room in which you have the clock. Step 2: Face towards the clock. Step 3: View the time.")
        if "name" in voice_data:
            speak("My file name is my name.")
            print("My file name is my name.")
        if "how to open a door" in voice_data:
            speak("Just push it. Done!")
            print("Just push it. Done!")

speech_by_us()
engine.runAndWait()

root.mainloop()