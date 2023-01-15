# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 18:19:31 2023

@author: laksh
"""

from tkinter import *
import speech_recognition as sr
import pyttsx3

root = Tk()
root.geometry("400x400")
engine = pyttsx3.init()

label_your_speech = Label(root)
label_computer_speech = Label(root)

def computer_say():
    engine.say("How can I help you? Suggested: How to open a door?")
    label_computer_speech["text"] = "How can I help you? Suggested: How to open a door?"

def speech_by_us():
    speech_by_you = sr.Recognizer()
    with sr.Microphone() as source:
        audio=speech_by_you.listen(source)
        voice_data = ''
        label_your_speech["text"] = voice_data
        try:
            voice_data = speech_by_you.recognize_google(audio, language="en-in")
        except sr.UnknownValueError:
            #Speech by computer
            engine.say("Can you please shout what you just said so that I can hear it.")
            print("Can you please shout what you just said so that I can hear it.")
        print(voice_data)
        if "time" in voice_data:
            engine.say("How to view time: Step 1: Walk to the room in which you have the clock. Step 2: Face towards the clock. Step 3: View the time.")
            label_computer_speech["text"] = "How to view time: Step 1: Walk to the room in which you have the clock. Step 2: Face towards the clock. Step 3: View the time."
        if "name" in voice_data:
            engine.say("My file name is my name.")
            label_computer_speech["text"] = "My file name is my name."
        if "how to open a door" in voice_data:
            engine.say("Just push it. Done!")
            label_computer_speech["text"] = "Just push it. Done!"

engine.runAndWait()

btn_listen = Button(root, text="Listen", font=(15), bg="Light green", fg="white", bd=0, command=speech_by_us)
btn_listen.place(relx=0.5, rely=0.2, anchor=CENTER)

computer_say()
root.mainloop()