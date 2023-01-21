# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 08:58:35 2023

@author: laksh
"""

from tkinter import *
import requests
import json

root = Tk()
root.geometry("300x300")
root.overrideredirect(True)
root.configure(bg="sky blue")

label1 = Label(root, text="Captial City Name", font=(15), bg="sky blue", fg="White")
label1.place(relx=0.4, rely=0.1, anchor=CENTER)
entry1 = Entry()
entry1.place(relx=0.35, rely=0.2, anchor=CENTER)
label2 = Label(root, text="Country: ", bg="sky blue", fg="white")
label2.place(relx=0.34, rely=0.4, anchor=CENTER)
label3 = Label(root, text="Region: ", bg="sky blue", fg="white")
label3.place(relx=0.34, rely=0.5, anchor=CENTER)
label4 = Label(root, text="Lanuage: ", bg="sky blue", fg="white")
label4.place(relx=0.34, rely=0.6, anchor=CENTER)
label5 = Label(root, text="Population: ", bg="sky blue", fg="white")
label5.place(relx=0.34, rely=0.7, anchor=CENTER)
label6 = Label(root, text="Area: ", bg="sky blue", fg="white")
label6.place(relx=0.34, rely=0.8, anchor=CENTER)

def get_info():
    api_request = requests.get("https://restcountries.com/v2/capital/" + entry1.get())
    print("https://restcountries.com/v2/capital/" + entry1.get())
    api_output_json = json.loads(api_request.content)
    print(api_output_json[0]['name'])
    label2["text"] += api_output_json[0]["nativeName"]
    label3["text"] += api_output_json[0]["region"]
    label4["text"] += api_output_json[0]["languages"][0]["name"]
    label5["text"] += str(api_output_json[0]["population"])
    label6["text"] += str(api_output_json[0]["area"])

btn1 = Button(root, text="Get info", command=get_info, bg="light green", fg="white", bd=0)
btn1.place(relx=0.25, rely=0.3, anchor=CENTER)

root.mainloop()