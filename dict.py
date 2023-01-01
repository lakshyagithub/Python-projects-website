from tkinter import *

root = Tk()
root.title("Dictionary")
root.geometry("600x400")
root.configure(background="sky blue")

label_of_mutable = Label(root)
label_of_immutable = Label(root)
label_of_tkinter = Label(root)

dict1 = {'mutable' : 'Values that can be changed like a list in python',
         'immutable' : 'Values that cannot be changed like a tuple in python',
         'tkinter' : 'It is a GUI library for python'}

def mutable():
    label_of_mutable['text'] = "Meaning: " + dict1['mutable']

def immutable():
    label_of_immutable['text'] = "Meaning: " + dict1['immutable']

def tkinter1():
    label_of_tkinter['text'] = "Meaning: " + dict1['tkinter']

#Buttons
btn_of_muteable = Button(root, text="Meaning of muteable", command=mutable, bg="Light green", fg="white", bd=0)
btn_of_immmuteable = Button(root, text="Meaning of immuteable", command=immutable, bg="Light green", fg="white", bd=0)
btn_of_tkinter = Button(root, text="Meaning of tkinter", command=tkinter1, bg="Light green", fg="white", bd=0)
btn_of_muteable.place(relx=0.5, rely=0.2, anchor=CENTER)
btn_of_immmuteable.place(relx=0.5, rely=0.4, anchor=CENTER)
btn_of_tkinter.place(relx=0.5, rely=0.6, anchor=CENTER)

#Placing lables
label_of_mutable.place(relx=0.5, rely=0.3, anchor=CENTER)
label_of_immutable.place(relx=0.5, rely=0.5, anchor=CENTER)
label_of_tkinter.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()