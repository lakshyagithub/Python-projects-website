from tkinter import *
import random

root = Tk()
root.title("Dictionary")
root.geometry("600x400")
root.configure(background="sky blue")

colors_names = {"colors" : ["maroon1","lawn green","magenta2","purple1","springgreen2","chocolate1", "deep pink","cyan", "sky blue"]}

def Random_func():
    random_no = random.randint(0, 8)
    dict_color = colors_names["colors"][random_no]
    print(dict_color)
    root.configure(background=dict_color)

btn = Button(root, text="Change background color", command=Random_func, bg="Light green", fg="white", bd=0)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()