from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root = Tk()
root.geometry("1200x450")
root.title("Time zone")

#------------------------------------India----------------------------------
label_india_text = Label(root, text="India")
Image_clock = ImageTk.PhotoImage(Image.open("clock.jpg"))
Image_clock_display = Label(root)
Image_clock_display["image"] = Image_clock
time_india = Label(root)

label_india_text.place(relx=0.2, rely=0.05, anchor=CENTER)
Image_clock_display.place(relx=0.2, rely=0.35, anchor=CENTER)
time_india.place(relx=0.2, rely=0.65, anchor=CENTER)

#------------------------------------USA----------------------------------
USA_text = Label(root, text="USA")
USA_clock = ImageTk.PhotoImage(Image.open("clock.jpg"))
USA_clock_display1 = Label(root)
USA_clock_display1["image"] = Image_clock
time_USA = Label(root)

USA_text.place(relx=0.7, rely=0.05, anchor=CENTER)
USA_clock_display1.place(relx=0.7, rely=0.35, anchor=CENTER)
time_USA.place(relx=0.7, rely=0.65, anchor=CENTER)

lol_text = Label(root, text="lol")
lol_clock = ImageTk.PhotoImage(Image.open("clock.jpg"))
lol_clock_display1 = Label(root)
lol_clock_display1["image"] = Image_clock
time_lol = Label(root)

lol_text.place(relx=0.7, rely=0.05, anchor=CENTER)
lol_clock_display1.place(relx=0.7, rely=0.35, anchor=CENTER)
time_lol.place(relx=0.7, rely=0.65, anchor=CENTER)

#--------------------------------MAIN CODE---------------------------------
class India:
    def times(self):
        home = pytz.timezone("Asia/Kolkata")
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        time_india["text"] = "Time:", current_time
        time_india.after(200, self.times)
        
class US:
    def times(self):
        home1 = pytz.timezone("US/Central")
        local_time1 = datetime.now(home1)
        current_time1 = local_time1.strftime("%H:%M:%S")
        time_USA["text"] = "Time:", current_time1
        time_USA.after(200, self.times)
        
obj_India = India()
obj_USA = US()
india_btn = Button(root, text="Show time", command=obj_India.times)
india_btn.place(relx=0.2, rely=0.8, anchor=CENTER)
us_btn = Button(root, text="Show time", command=obj_USA.times)
us_btn.place(relx=0.7, rely=0.8, anchor=CENTER)

root.mainloop()
