
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 20:58:28 2022

@author: laksh
"""

from tkinter import *
import random

root = Tk()
root.geometry("400x200")
root.title("Colors")
root.configure(background="sky blue")

label1 = Label(root, bg="sky blue", font=("Arial", 40), fg="green")
label1.pack()

text_box = Entry()
text_box.place(relx=0.5, rely=0.5, anchor=CENTER)

class game:
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.text = ["blue", "green", "yellow"]
        self.random_color = random.randint(0, 2)
        self.color = ["orange", "red", "black"]
        label1["text"] = self.text[self.random_color]
        label1["fg"] = self.color[self.random_color]
        print(self.text[self.random_color])
        print(self.color[self.random_color])
    def checkAnswer(self):
        self.random_text = self.text[self.random_color]
        print(self.random_text)
        if text_box.get() == self.random_text:
            print("Correct!")

obj1 = game()

btn1 = Button(root, text="Start/Update color", command=obj1.updateGame, font=(15), bg="light green", fg="white", bd=0)
btn1.place(relx=0.7, rely=0.7, anchor=CENTER)
btn2 = Button(root, text="Check", command=obj1.checkAnswer, font=(15), bg="light green", fg="white", bd=0)
btn2.place(relx=0.2857142857142857, rely=0.7, anchor=CENTER)

root.mainloop()