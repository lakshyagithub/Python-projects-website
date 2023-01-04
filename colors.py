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

label1 = Label(root, bg="sky blue", font=(40), fg="green")
label1.pack()

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

obj1 = game()

btn1 = Button(root, text="Start", command=obj1.updateGame, font=(15), bg="light green", fg="white", bd=0)
btn1.place(relx=0.7, rely=0.7, anchor=CENTER)

root.mainloop()