# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 10:58:36 2022

@author: laksh
"""

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("clases")
root.geometry("400x400")

dropdowndata = ["label", "button", "dropdown"]
dropdown = ttk.Combobox(root, state="readonly", values=dropdowndata)

class create_element1:
    def __init__(self):
        print("awesome")
    def buildbutton(self):
        class_btn = Button(root, text="Click me!", command=self.message)
        class_btn.pack(padx=20, pady=10)
    def buildlabel(self):
        class_label = Label(root, text="Some text...")
        class_label.pack(padx=20, pady=10)
    def builddropdown(self):
        values1 = ["<none>", "option1", "option2"]
        class_d1 = ttk.Combobox(root, state="readonly", values=values1)
        class_d1.pack(padx=20, pady=10)
    def message(self):
        messagebox.showinfo("Awesome prompt!", "Awesome!")
    def onclick1(self):
        if (dropdown.get() == "label"):
            self.buildlabel()
        if (dropdown.get() == "dropdown"):
            self.builddropdown()
        if (dropdown.get() == "button"):
            self.buildbutton()
        

create_element1_caller = create_element1()
btn1 = Button(root, text="Build!", command=create_element1_caller.onclick1)
dropdown.pack(padx=20, pady=10)
btn1.pack(padx=20, pady=10)

root.mainloop()