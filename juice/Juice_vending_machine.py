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
    
orderJuice()

root.mainloop()