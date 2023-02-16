from tkinter import *
from PIL import ImageTk, Image
from firebase import firebase as fb
from simplecrypt import encrypt, decrypt

firebase = fb.FirebaseApplication("https://test-34dca-default-rtdb.firebaseio.com/", None)
login_window = Tk()
login_window.geometry("400x400")
login_window.config(bg='sky blue')

windows_img = ImageTk.PhotoImage(Image.open("start.png"))

username = ""
your_code = ""
your_friends_code = ""
message_entry = ""
message_text = ""
last_value = ""

def sendData():
    global username
    global your_code
    global message_entry
    message = username + " : " + message_entry.get()
    chiper_code = encrypt("LAKSHYA", message)
    hex_string = chiper_code.hex()
    put_date = firebase.put("/", your_code, hex_string)
    print(put_date)
    getData()
    
def getData():
    global message_text
    global last_value
    global your_code
    global your_friends_code
    get_your_data = firebase.get("/", your_code)
    print(get_your_data)
    byte_str = bytes.fromhex(get_your_data)
    orginal = decrypt("LAKSHYA", byte_str)
    print("Orginal data : ", orginal)
    final_message = orginal.decode("utf-8")
    message_text.insert(END, final_message+"\n")
    
    get_friends_data = firebase.get("/", your_friends_code)
    if(get_friends_data != None):
        print("data : ",get_friends_data)
        byte_str = bytes.fromhex(get_friends_data)
        original = decrypt('LAKSHYA', byte_str)
        final_message = original.decode("utf-8")
        if (final_message not in last_value):
            print(final_message)
            message_text.insert(END, final_message+"\n")
            last_value = final_message
    

def enterRoom():
    global username
    global your_code
    global your_friends_code
    global message_entry
    global message_text
    your_code = your_code_entry.get()
    your_friends_code = friends_code_entry.get()
    username = username_entry.get()
    login_window.destroy()
    
    print(your_code)
    print(your_friends_code)
    print(username)
    
    message_window = Tk()
    message_window.config(bg='sky blue')
    message_window.geometry("600x500")
    
    message_text = Text(message_window, height=20, width=72)
    message_text.place(relx=0.5,rely=0.35, anchor=CENTER)
    
    message_label = Label(message_window, text="Message " , font = 'arial 13', bg='sky blue', fg="white")
    message_label.place(relx=0.3,rely=0.8, anchor=CENTER)
    
    message_entry = Entry(message_window, font = 'arial 15')
    message_entry.place(relx=0.6,rely=0.8, anchor=CENTER)
    
    btn_send = Button(message_window, text="Send", font = 'arial 13', bg="light green", fg="white", padx=10, bd=0, command=sendData)
    btn_send.place(relx=0.5,rely=0.9, anchor=CENTER)
    
    message_window.mainloop()
    

username_label = Label(login_window, text="Username : " , font = 'arial 13', bg ='sky blue', fg="white")
username_label.place(relx=0.3,rely=0.3, anchor=CENTER)

username_entry = Entry(login_window)
username_entry.place(relx=0.6,rely=0.3, anchor=CENTER)

your_code_label = Label(login_window, text="Your code :  " , font = 'arial 13', bg ='sky blue', fg="white")
your_code_label.place(relx=0.3,rely=0.4, anchor=CENTER)

your_code_entry = Entry(login_window)
your_code_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

friends_code_label = Label(login_window, text="Your Friends code :  " , font = 'arial 13', bg ='sky blue', fg="white")
friends_code_label.place(relx=0.22,rely=0.5, anchor=CENTER)

friends_code_entry = Entry(login_window)
friends_code_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_start = Button(login_window, text="Start" , font = 'arial 13' , bg="light green", fg="white", command=enterRoom, bd=0, padx=10, image=windows_img)
btn_start.place(relx=0.5,rely=0.65, anchor=CENTER)

login_window.mainloop()
