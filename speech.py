# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 19:48:12 2023

@author: laksh
"""

import speech_recognition as sr

def speech_by_us():
    speech_by_you = sr.Recognizer()
    with sr.Microphone() as source:
        audio=speech_by_you.listen(source)
        voice_data = ''
        try:
            voice_data = speech_by_you.recognize_google(audio, language="en-in")
        except sr.UnknownValueError:
            #Speech by computer
            print("Can you please shout what you just said so that I can hear it.")
        print(voice_data)

speech_by_us()