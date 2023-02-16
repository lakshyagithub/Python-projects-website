from simplecrypt import encrypt, decrypt
from tkinter import *
from firebase import firebase

firebase = firebase.FirebaseApplication("https://test-34dca-default-rtdb.firebaseio.com/", None)

login_window = Tk()
login_window.geometry("400x400")
login_window.config(bg='#AB92BF')

username = ''
your_code = ''
your_friends_code = ''
message_text = ''
message_entry = ''
last_value = ''

def getData():
    global message_text
    global last_value
    global your_code
    global your_friends_code
    get_your_data = firebase.get('/', your_code)
    print(get_your_data)
    byte_str = bytes.fromhex(get_your_data)
    original = decrypt('AIM', byte_str)
    print("Original data ",original)
    final_message = original.decode("utf-8")
    print(final_message)
    message_text.insert(END, final_message+"\n")
   
    get_friends_data = firebase.get('/', your_friends_code)
    if(get_friends_data != None):
        print("data : ",get_friends_data)
        byte_str = bytes.fromhex(get_friends_data)
        original = decrypt('AIM', byte_str)
        final_message = original.decode("utf-8")
        if (final_message not in last_value):
            print(final_message)
            message_text.insert(END, final_message+"\n")
            last_value = final_message
 
def sendData():
    global username
    global message_entry
    global your_code
    message = username+ " : "+message_entry.get()
    ciphercode = encrypt('AIM', message)
    hex_string = ciphercode.hex()
    put_date = firebase.put("/", your_code, hex_string)
    print(put_date)
    getData()

def enterRoom():
    global username
    global your_code
    global your_friends_code
    global message_entry
    global message_text
    your_code = your_code_entry.get()
    your_friends_code = friends_code_entry.get()
    username = username_entry.get()
   
    message_window = Tk()
    message_window.config(bg='#AFC1D6')
    message_window.geometry("600x500")
    message_text = Text(message_window, height=20, width=72)
    message_text.place(relx=0.5,rely=0.35, anchor=CENTER)
   
    message_label = Label(message_window, text="Message " , font = 'arial 13', bg='#AFC1D6', fg="white")
    message_label.place(relx=0.3,rely=0.8, anchor=CENTER)
   
    message_entry = Entry(message_window, font = 'arial 15')
    message_entry.place(relx=0.6,rely=0.8, anchor=CENTER)
   
    btn_send = Button(message_window, text="Send", font = 'arial 13', bg="#D6CA98", fg="black", padx=10, relief=FLAT ,command = sendData)
    btn_send.place(relx=0.5,rely=0.9, anchor=CENTER)
   
    login_window.destroy()
    message_window.mainloop()
   

username_label = Label(login_window, text="Username : " , font = 'arial 13', bg ='#AB92BF', fg="white")
username_label.place(relx=0.3,rely=0.3, anchor=CENTER)

username_entry = Entry(login_window)
username_entry.place(relx=0.6,rely=0.3, anchor=CENTER)

your_code_label = Label(login_window, text="Your code :  " , font = 'arial 13', bg ='#AB92BF', fg="white")
your_code_label.place(relx=0.3,rely=0.4, anchor=CENTER)

your_code_entry = Entry(login_window)
your_code_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

friends_code_label = Label(login_window, text="Your Friends code :  " , font = 'arial 13', bg ='#AB92BF', fg="white")
friends_code_label.place(relx=0.22,rely=0.5, anchor=CENTER)

friends_code_entry = Entry(login_window)
friends_code_entry.place(relx=0.6,rely=0.5, anchor=CENTER)


btn_start = Button(login_window, text="Start" , font = 'arial 13' , bg="#CEF9F2", fg="black", command=enterRoom, relief=FLAT, padx=10)
btn_start.place(relx=0.5,rely=0.65, anchor=CENTER)

login_window.mainloop()
