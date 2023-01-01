from tkinter import *
import random

root = Tk()
root.geometry("400x400")
root.title("Safe password generator")
root.configure(background="sky blue")

label1 = Label(root)
array_3D = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], ["your", "password", "is", "with", "the", "HACKER"], ["A", "B", "C", "D", "E", "F", "G", "H"]]]

def generate_password():
    array_3D1 = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], ["your", "password", "is", "with", "the", "HACKER"], ["A", "B", "C", "D", "E", "F", "G", "H"]]]
    random_1 = random.randint(0, 9)
    random_2 = random.randint(0, 5)
    random_3 = random.randint(0, 7)

    a = str(array_3D1[0][0][random_1])
    b = (array_3D1[0][1][random_2])
    c = (array_3D1[0][2][random_3])
    #label1["text"] = "New password: " + a + b + c
    print("New password: ", a + b + c)

btn = Button(root, text="Show new password", command=generate_password, bg="light green", fg="white", bd=0)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
label1.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()