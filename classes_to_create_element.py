# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 17:16:00 2022

@author: laksh
"""

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("clases")
root.geometry("400x400")

class class1ok:
    def __init__(self):
        print("Nothing to see here...")
    def create_new_element(self):
        label1 = Label(root, text="My job is to do nothing here, just to be cloned...", fg="red")
        label1.pack()
        btn1 = Button(root, text="Hi, I am his brother. He likes to act.", command=self.call_my_friend)
        btn1.pack(padx=20, pady=10)
    def call_my_friend(self):
        messagebox.showwarning("Hey!", "Don't click on my friend or I will hack you.")

the_people_in_the_class = class1ok()
btn2 = Button(root, text="Build a class which talks!", command=the_people_in_the_class.create_new_element)
btn2.pack(padx=20, pady=10)
root.mainloop()