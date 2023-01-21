from tkinter import *
import requests
import json

root=Tk()
root.title("My Weather App")
root.geometry("350x300")
root.overrideredirect(True)
root.configure(background="sky blue")
#Setting labels
city_name_label=Label(root, text="City Name",font=("Helvetica", 18,'bold'),bg="sky blue", fg="white")
city_name_label.place(relx=0.28,rely=0.15,anchor=CENTER)

city_entry=Entry(root)
city_entry.place(relx=0.28,rely=0.35,anchor=CENTER)

weather_info_label = Label(root,text="Weather: ", bg="light green", fg="white", font=("bold", 10))
weather_info_label.place(relx=0.23,rely=0.6,anchor=CENTER) 

humidity_info_label = Label(root,text="Humidity: ", bg="light green", fg="white", font=( "bold",10)) 
humidity_info_label.place(relx=0.22,rely=0.7,anchor=CENTER)

#Main funciton
def weather_get_ok():
    api_signal = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city_entry.get() + "&appid=21cab08deb7b27f4c2b55f3e2df28ea4")
    print("https://api.openweathermap.org/data/2.5/weather?q=" + city_entry.get() + "&appid=21cab08deb7b27f4c2b55f3e2df28ea4")
    api_signal_out = json.loads(api_signal.content)
    weather_get = 

search_btn = Button(root, text="search", bg="light green", fg="white", bd=0, command=weather_get_ok)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)

root.mainloop()
