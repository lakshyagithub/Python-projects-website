# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:23:57 2022

@author: laksh
"""
from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

root = Tk()
root.title("Ronald")
root.geometry("900x500")

burger = ImageTk.PhotoImage(Image.open("burger1.png"))
burger_image = Label(root)
burger_image["image"] = burger
burger_image.place(relx=0.7, rely=0.5, anchor=CENTER)

label_heading = Label(root, text="Ronald", font=("times", 40, "bold"), fg="Orange")
label_heading.place(relx=0.12, rely=0.1, anchor=CENTER)

dish=["Burger", "dishtv"]
dish_dropdown = ttk.Combobox(root, state="readonly", values=dish)
dish_dropdown.place(relx=0.25, rely=0.2, anchor=CENTER)

label_select_addons=Label(root, text="Select Add-ons", font=("times", 15))
label_select_addons.place(relx=0.08, rely=0.5, anchor=CENTER)

toppings = []
toppings_dropdown = ttk.Combobox(root, state="readonly", values=toppings)
toppings_dropdown.place(relx=0.25, rely=0.5, anchor=CENTER)

dish_ammount=Label(root, font=("times", 15, "bold"))
dish_ammount.place(relx=0.2, rely=0.75, anchor=CENTER)



class hotel():
    def __init__(self):
        print("Current Version 1.0 beta")
    def menu(dish):
        if dish=="burger":
            print("You can choose the following:")
            print("Full cheese | Full Bread")
        elif dish=="dishtv":
            print("You can choose the following plans:")
            print("5GB data | 1TB data")
        else:
            print("Ok so you don't want a data plan or a burger? \n \n \n \n \n \n \n \n \n \n \n \n \n")
    
    def final_ammount(dish, add_ons):
        if dish=="burger" and add_ons=="Full cheese":
            print("Pay ₹900")
        if dish=="burger" and add_ons=="Full Bread":
            print("pay ₹900")
        if dish=="dishtv" and add_ons=="5GB data":
            print("Pay ₹90,000")
        if dish=="dishtv" and add_ons=="1TB data":
            print("Pay ₹10,00,000")

class child1(hotel):
    def __init__(self, dish):
        self.new_dish = dish
    def get_menu(self):
        hotel.menu(new_dish)

#class child2(hotel):
#    
root.mainloop()