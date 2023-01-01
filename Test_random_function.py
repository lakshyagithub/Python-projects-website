from tkinter import *
import random

root = Tk()
root.geometry("400x400")
root.title("Test random function")
root.configure(background="sky blue")

input_box = Entry(root)
label1 = Label(root, text="Generated password: ")
label2 = Label(root, text="Guessed password: ")
array_3D = [[[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], ["your", "password", "is", "with", "the", "HACKER"], ["A", "B", "C", "D", "E", "F", "G", "H"]]]

def generate_password():
    label2["text"] += ""
    input_data = input_box.get()
    label2["text"] += str(input_data)

    random_1 = random.randint(0, 9)
    random_2 = random.randint(0, 5)
    random_3 = random.randint(0, 7)

    a = str(array_3D[0][0][random_1])
    b = (array_3D[0][1][random_2])
    c = (array_3D[0][2][random_3])
    label1["text"] = "Generated password: " + a + b + c

btn = Button(root, text="Show new password", command=generate_password, bg="light green", fg="white", bd=0)
input_box.place(relx=0.5, rely=0.4, anchor=CENTER)
label2.place(relx=0.5, rely=0.5, anchor=CENTER)
btn.place(relx=0.5, rely=0.6, anchor=CENTER)
label1.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()