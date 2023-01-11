# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 18:22:58 2023

@author: laksh
"""

from tkinter import *

root = Tk()
root.title("Trans - The Lanuage Translator")
root.geometry("900x600")
root.configure(bg="Sky blue")

label_title = Label(root, text="Trans - The Lanuage Translator", font=("Segoe UI Semibold", 20), bg="Sky blue", fg="White")
label_title.pack()

text_area = Text(root, bg="White", fg="Black", bd=0, height=20, width=30, font=("Arial", 15))
text_area.place(relx=0.2, rely=0.5, anchor=CENTER)

root.mainloop()