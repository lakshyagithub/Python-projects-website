# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 21:02:05 2023

@author: laksh
"""

from tkinter import *
import json
import requests

root = Tk()
root.geometry("600x300")
root.overrideredirect(True)

api_req = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=e96629e9d083487b89a5b1491b56f784")
api_output_json = json.loads(api_req.content)

label1 = Label(root, text=api_output_json["articles"][0]["author"])
label1.pack()

label2 = Label(root, text=api_output_json["articles"][0]["title"])
label2.pack()

label3 = Label(root, text=api_output_json["articles"][0]["description"])
label3.pack()

root.mainloop()