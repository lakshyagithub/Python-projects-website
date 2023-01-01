from tkinter import *
import random

root = Tk()
root.geometry("400x400")
root.title("Country Captial List")

list1 = []
list2 = []

input1 = Entry(root)
input2 = Entry(root)
list1_label = Label(root)
list2_label = Label(root)
random_list1_label = Label(root)
random_list2_label = Label(root)

def dosomthing():
    input1_data = input1.get()
    input2_data = input2.get()
    list1.append(input1_data)
    list2.append(input2_data)
    list1_label["text"] = "Country List:" + str(list1)
    list2_label["text"] = "Country Captial List: " + str(list2)

def dosomthing2():
    random_number1 = random.randint(0, (len(list1)-1))
    random_number2 = random.randint(0, (len(list2)-1))
    text1 = list1[random_number1]
    text2 = list2[random_number2]
    random_list1_label["text"] = "Random Country: " + str(text1)
    random_list2_label["text"] = "Random Country Captial: " + str(text2)

btn = Button(root, text="Ok", command=dosomthing, bd=0, bg="blue", fg="white")
btn1 = Button(root, text="Show Random", command=dosomthing2, bd=0, bg="blue", fg="white")
input1.place(relx=0.5, rely=0.2, anchor=CENTER)
input2.place(relx=0.5, rely=0.3, anchor=CENTER)
list1_label.place(relx=0.5, rely=0.4, anchor=CENTER)
list2_label.place(relx=0.5, rely=0.5, anchor=CENTER)
btn.place(relx=0.5, rely=0.6, anchor=CENTER)
random_list1_label.place(relx=0.5, rely=0.7, anchor=CENTER)
random_list2_label.place(relx=0.5, rely=0.8, anchor=CENTER)
btn1.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()