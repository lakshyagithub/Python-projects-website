from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root_icon = PhotoImage(file="start_point1.png")
root.iconphoto(False, root_icon)
root.title("Canvas")
root.geometry("600x600")

color_label = Label(root, text="Pen-down Color: ", font=("comic sans ms", 12))
color_label.place(relx=0.6, rely=0.9, anchor=CENTER)

input_box = Entry(root)
input_box.insert(0, "black")
input_box.place(relx=0.8, rely=0.9, anchor=CENTER)

canvas1 = Canvas(root, width=590, height=510, bg="white", highlightbackground="lightgray")
canvas1.pack()

direction = ""
oldx = 0
oldy = 0
newx = 0
newy = 0

def right_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newx = newx+5
    direction = "right"
    draw(direction, oldx, oldy, newx, newy)

def left_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newx = newx-5
    direction = "left"
    draw(direction, oldx, oldy, newx, newy)
    
def up_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newy = newy-5
    direction = "up"
    draw(direction, oldx, oldy, newx, newy)
    
def down_dir(event):
    global direction
    global oldx
    global oldy
    global newx
    global newy
    oldx = newx
    oldy = newy
    newy = newy+5
    direction = "down"
    draw(direction, oldx, oldy, newx, newy)
    
def draw(direction, oldx, oldy, newx, newy):
    

root.bind("<Right>", right_dir)
root.bind("<Left>", left_dir)
root.bind("<Up>", up_dir)
root.bind("<Down>", down_dir)

root.mainloop()
