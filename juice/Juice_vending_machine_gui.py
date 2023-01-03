# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 19:24:36 2023

@author: laksh
"""

from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

gui = Tk()
gui.geometry("800x600")
gui.title("Juice vending machine🥤")
gui.configure(bg="orange2")

label_heading = Label(gui, text="Juice Center", bg="orange2", font=("Sylfaen", 18, "bold", "italic"))
label_heading.place(relx=0.05, rely=0.1, anchor=W)

logo_shop_img = ImageTk.PhotoImage(Image.open("logo.png"))
logo_shop = Label(gui, image=logo_shop_img, bg="orange2")
logo_shop.place(relx=0.2, rely=0.4, anchor=CENTER)

class juice:
    def __init__(self, fruit_name, qty1):
        self.fruit_name = fruit_name
        self.qty1 = int(qty1)
        self.__cost = 250
    def __calcCost(self):
        total_cost = self.qty1 * self.__cost
        print("You have to pay ₹" + str(total_cost))
        if(self.fruit_name == "Apple"):
            calorie = self.qty1 * 52
        if(self.fruit_name == "Mango"):
            calorie = self.qty1 * 60
        if(self.fruit_name == "Orange"):
            calorie = self.qty1 * 47
        print("x" + str(self.qty1) + " = " + str(calorie) + " calorie")
    def getCost(self):
        self.__calcCost()

def orderJuice():
    fruit = "Mango"
    qty2 = 200
    obj_shop = juice(fruit, qty2)
    obj_shop.getCost()
    
#orderJuice()

gui.mainloop()