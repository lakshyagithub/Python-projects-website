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
root.configure(background="White")

label1 = Label(root, bg="white", font=(15), fg="green")
label1.pack()

class game:
    def __init__(self):
        self.__score = 0
    def updateGame(self):
        self.text = ["blue", "green", "yellow"]
        self.random_color = 

root.mainloop()