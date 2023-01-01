# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 19:34:39 2022

@author: laksh
"""

from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

root = Tk()
root.geometry("800x600")
root.title("Juice vending machine🥤")
iconsfive = PhotoImage(file="icons8-tropical-drink-96.png")
root.iconphoto(False, iconsfive)

class juice:
    def __init__(self, fruit_name, qty1):
        self.fruit_name = fruit_name
        self.qty1 = int(qty1)
        self.__cost = 250
    def calcCost(self):
        total_cost = self.qty1 * self.__cost
        print("You have to pay ₹" + str(total_cost))
        if(self.fruit_name == "Apple"):
            
        
root.mainloop()