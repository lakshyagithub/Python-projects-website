from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Thomas's result")
root.configure(background="Light Green")

array_2D = [["John", "A", "Excellent"], ["James", "B", "Very Good"], ["Thomas", "C", "Good"]]
label1 = Label(root)

def update():
    label1["text"] = array_2D[2][0] + " got grade: " + array_2D[2][1] + " and is doing " + array_2D[2][2]

btn = Button(root, text="Show result", command=update, bg="sky blue", fg="white", bd=0)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
label1.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()