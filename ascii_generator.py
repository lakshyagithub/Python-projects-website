from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Ascii generator")
root.configure(background="light green")

enter_word = Entry(root)
ins_label = Label(root, text="Name in ASCII: ", bg="light yellow", fg="black")

enter_word.place(relx=0.5, rely=0.4, anchor=CENTER)
ins_label.place(relx=0.5, rely=0.6, anchor=CENTER)

def con():
    ins_label["text"] = "Name in ASCII: "
    input_word = enter_word.get()
    for letter in input_word:
        ins_label["text"] += str(ord(letter)) + "  "

btn = Button(root, text="Show entered word in ASCII", command=con, bg="gold", fg="black")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()