# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 18:41:31 2022

@author: laksh
"""

from tkinter import *
import speedtestpy

root = Tk()
icon1 = PhotoImage(file="icons8-ookla-speedtest-420.png")
root.iconphoto(False, icon1)
root.config(bg="#dee8f1")
root.title("Seed - Network speedtest program")
root.geometry("500x300")

label = Label(root, text="Internet Speed Check", font=("Lucida Sans Unicode", 20, "bold", "italic"), fg="#5D6D7E", bg="#dee8f1")
label.place(relx=0.5, rely=0.1, anchor=CENTER)

label_download = Label(root, text="Download Speed ↓", font=("Segoe Print", 18, "bold"), fg="#1E8449", bg="#dee8f1")
label_download.place(relx=0.25, rely=0.5, anchor=CENTER)

label_upload = Label(root, text="Upload Speed ↑", font=("Segoe Print", 18, "bold"), fg="#9B59B6", bg="#dee8f1")
label_upload.place(relx=0.75, rely=0.5, anchor=CENTER)

label_download_speed = Label(root, font=("Yu Gothic Light", 14, "bold"), bg="#dee8f1")
label_download_speed.place(relx=0.25, rely=0.6, anchor=CENTER)

label_upload_speed = Label(root, font=("Yu Gothic Light", 14, "bold"), bg="#dee8f1")
label_upload_speed.place(relx=0.25, rely=0.6, anchor=CENTER)

def speedtest():
    print("Hi")
    st = speedtest.Speedtest()
    download_speed = round(st.download()/1000000, 2)
    label_download_speed["text"] = str(download_speed) + "mbps"
    upload_speed = round(st.upload()/1000000, 2)
    label_upload_speed["text"] = str(upload_speed) + "mbps"
    
btn_doctor = Button(root, text="Check speed", bg="#218796", fg="white", bd=0, command=speedtest)
btn_doctor.place(relx=0.5, rely=0.3, anchor=CENTER)

root.mainloop()