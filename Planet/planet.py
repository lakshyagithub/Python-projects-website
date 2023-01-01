from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

root = Tk()
root.title("About planets")
root.geometry("500x500")
icon1 = PhotoImage(file="Logo.png")
root.iconphoto(False, icon1)
root.configure(background="sky blue")

earth1 = ImageTk.PhotoImage(Image.open("earth.jpg"))
mercury1 = ImageTk.PhotoImage(Image.open("mercury.jpg"))
venus1 = ImageTk.PhotoImage(Image.open("venus.jpg"))

label_planet = Label(root, bg="sky blue", font=("Comic Sans MS", 12, "bold"), text="Planet: ")
label_planet_name = Label(root, bg="sky blue", font=("Comic Sans MS", 12, "bold"), text="")
label_planet_image = Label(root, bg="red", highlightthickness=5, borderwidth=2, relief=SOLID)
label_planet_gravity = Label(root, bg="sky blue", font=("Comic Sans MS", 12, "bold"), text="gravity: ")
label_planet_info = Label(root, bg="sky blue", font=("Comic Sans MS", 12, "bold"), wraplength=500)

planets1 = ["Mercury", "Venus", "Earth"]
selectedvalue = StringVar()
dropdown1 = ttk.Combobox(root, values=planets1, textvariable=selectedvalue)

def showinfoplanets():
    global selectedvalue
    planet = selectedvalue.get()
    print(planet)
    if planet == "Mercury":
        label_planet_name["text"] = "Mercury"
        label_planet_image["image"] = mercury1
        label_planet_info["text"] = "Information - Mercury is the smallest planet in our solar system. It's just a little bigger than Earth's moon"
        label_planet_gravity["text"] = "Gravity and radius - Gravity : 3.7 m/s² \n Radius : 2,439.7 km"
    elif planet == "Venus":
        label_planet_name["text"] = "Venus"
        label_planet_image["image"] = venus1
        label_planet_info["text"] = "Information - Venus is the brightest object in the sky after the Sun and the Moon, and sometimes looks like a bright star in the morning or evening sky."
        label_planet_gravity["text"] = "Gravity and radius - Gravity : 8.87 m/s² \n Radius : 6,051.8 km"
    elif planet == "Earth":
        label_planet_name["text"] = "Earth"
        label_planet_image["image"] = earth1
        label_planet_info["text"] = "Information - Earth is the only place in the known universe confirmed to host life and it's the only one known for sure to have liquid water on its surface."
        label_planet_gravity["text"] = "Gravity and radius - Gravity : 9.807 m/s² \n Radius : 6,371 km"


btn = Button(root, text="Show planet info", command=showinfoplanets, bd=0, bg="light green", font=("Comic Sans MS", 12, "bold"))

label_planet.place(relx=0.2, rely=0.1, anchor=CENTER)
dropdown1.place(relx=0.5, rely=0.1, anchor=CENTER)
btn.place(relx=0.5, rely=0.18, anchor=CENTER)
label_planet_name.place(relx=0.5, rely=0.25, anchor=CENTER)
label_planet_image.place(relx=0.5, rely=0.5, anchor=CENTER)
label_planet_gravity.place(relx=0.5, rely=0.8, anchor=CENTER)
label_planet_info.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()
