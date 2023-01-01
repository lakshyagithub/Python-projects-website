from tkinter import *
import random

root = Tk()
root.geometry("400x400")
root.title("Lucky Friend Wheel")
root.configure(bg="light green")

input_box = Entry(root)
list_display = Label(root)
Lucky_friend = Label(root)

list1 = []
print("Type of list 1: ", type(list1))

def add_to_list1():
    input_box_data = input_box.get()
    list1.append(input_box_data)
    list_display["text"] = "Your friends are: " + str(list1)

def random_numbers():
    random_number = random.randint(0, (len(list1)-1))
    print(random_number)
    friend = list1[random_number]
    print("Lucky Friend: ", friend)
    Lucky_friend["text"] = "Lucky Friend: " + friend
    

btn = Button(root, text="Who is my Lucky Friend?", command=random_numbers, bd=0, background="sky blue")
btn1 = Button(root, text="Add To The List", command=add_to_list1, bd=0, background="sky blue")

input_box.place(relx=0.5, rely=0.2, anchor=CENTER)
btn1.place(relx=0.5, rely=0.3, anchor=CENTER)
list_display.place(relx=0.5, rely=0.4, anchor=CENTER)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
Lucky_friend.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()