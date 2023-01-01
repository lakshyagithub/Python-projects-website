from tkinter import *
import random

root = Tk()
root.geometry("400x400")
root.title("List")

random_number_list = Label(root)
random_number_sorted_list = Label(root)

def randomlist1():
    randomlist = random.sample(range(10, 30), 5)
    random_number_list["text"] = "Random list: " + str(randomlist)
    randomlist.sort()
    random_number_sorted_list["text"] = "Sorted numbers: " + str(randomlist)

btn = Button(root, text="generate random list", command=randomlist1)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
random_number_list.place(relx=0.5, rely=0.5, anchor=CENTER)
random_number_sorted_list.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()