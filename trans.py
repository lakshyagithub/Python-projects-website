# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 18:22:58 2023

@author: laksh
"""

from tkinter import *
import speech_recognition as sr
from googletrans import Translator
import pyttsx3

root = Tk()
root.title("Trans - The Lanuage English To Hindi Translator")
root.geometry("900x600")
root.configure(bg="Sky blue")
trans1 = Translator()
engine = pyttsx3.init()

label_title = Label(root, text="Trans - The Lanuage English To Hindi Translator", font=("Segoe UI Semibold", 20), bg="Sky blue", fg="White")
label_title.pack()

text_area1 = Text(root, bg="White", fg="Black", bd=0, height=20, width=30, font=("Arial", 15))
text_area1.place(relx=0.2, rely=0.5, anchor=CENTER)

text_area2 = Text(root, bg="White", fg="Black", bd=0, height=20, width=30, font=("Arial", 15))
text_area2.place(relx=0.8, rely=0.5, anchor=CENTER)

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
        text_area1.delete(1.0, END)
        text_area1.insert(INSERT, voice_data)
        
def translated_function():
    text1 = text_area1.get(1.0, END)
    translated1 = trans1.translate(text1, src="en", dest="hi")
    text_area2.delete(1.0, END)
    text_area2.insert(END, translated1.text)
    engine.say(translated1)

btn_listen = Button(root, text="Listen", font=(10), bg="light green", fg="white", bd=0, command=speech_by_us)
btn_listen.place(relx=0.5, rely=0.5, anchor=CENTER)

btn_listen = Button(root, text="Translated", font=(10), bg="light green", fg="white", bd=0, command=translated_function)
btn_listen.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()