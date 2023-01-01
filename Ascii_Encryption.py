from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("ENCRYPTION WITH ASCII CODE")
root.configure(background="#bfefff")

input_box = Entry(root)
label1 = Label(root, text="Name in ASCII: ",bg="#e0ffff", fg="black")
label2 = Label(root, text="Encrypted Name: ",bg="#e0ffff", fg="black")

def encryption():
    input_data = input_box.get()
    label1["text"] = "Name in ASCII: "
    label2["text"] = "Encrypted Name: "

    for letter in input_data :
        label1["text"] += str(ord(letter)) + "  "
        user_letter = int(ord(letter))
        encrypt = user_letter - 1
        label2["text"] += str(chr(encrypt))

btn = Button(root, text="Enter", command=encryption)
input_box.place(relx=0.5, rely=0.3, anchor=CENTER)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
label1.place(relx=0.5, rely=0.5, anchor=CENTER)
label2.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()