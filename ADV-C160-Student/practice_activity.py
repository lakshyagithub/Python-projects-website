from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.minsize(600, 400)
root.maxsize(600, 500)

save_img = ImageTk.PhotoImage(Image.open("save.png"))
open_file_img = ImageTk.PhotoImage(Image.open("open.png"))
exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))

label_file_name = Label(root, text="File name: ")
label_file_name.place(relx=0.3,rely=0.1,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.5,rely=0.1, anchor= CENTER)

my_text= Text(root,height=5,width=40)
my_text.place(relx=0.5,rely=0.4,anchor= CENTER)


# Define clearInputFeild() function
def clearInputFeild():
    input_file_name.delete(0, END)

# Define clearTextarea() function
def clearTextarea():
    my_text.delete(1.0, END)

# Define addData() function
def addData():
    input_file_name.insert(END, "myfile")


open_button=Button(root,text="Clear Input field", command=clearInputFeild)
open_button.place(relx=0.25,rely=0.7,anchor=CENTER)
save_button=Button(root, text="Clear Textarea", command=clearTextarea)
save_button.place(relx=0.455,rely=0.7,anchor= CENTER)
exit_button=Button(root, text="Add data to input feild", command=addData)
exit_button.place(relx=0.7,rely=0.7,anchor= CENTER)

root.mainloop()

