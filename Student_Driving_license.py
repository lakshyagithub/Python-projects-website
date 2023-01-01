# Basic tkinter template
from logging import root
from tkinter import *

root = Tk()
root.title = "Driving License"
root.geometry = "200x400"

root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID : ")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth : ")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. : ")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address : ")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles : ")

# Create all the labels required to be displayed
label_id = Label(root)
label_dob = Label(root)
label_name = Label(root)
label_pin = Label(root)
label_address = Label(root)
label_vehicle_type = Label(root)

# Define the function
def showlicense():
    name = "winnie the pooh"
    print(type(name))
    license_id = 123456789
    print(type(license_id))
    date_of_birth = "October 14, 1926"
    print(type(date_of_birth))
    pin_no = 000000
    print(type(pin_no))
    address = "123 anystreet, anytown C A 1234"
    print(type(address))
    can_drive = ["car", "bike"]
    print(type(can_drive))

    label_name["text"] = name
    label_id["text"] = license_id
    label_address["text"] = address
    label_pin["text"] = pin_no
    label_dob["text"] = date_of_birth
    label_vehicle_type["text"] = can_drive


# Create a button
button1 = Button(root, text="Show my Driving License", command=showlicense)
button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()

# tkinter basic template end statement
root.mainloop()