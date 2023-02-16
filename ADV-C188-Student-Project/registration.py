import hashlib 
from tkinter import *
from tkinter import messagebox
from firebase import firebase

registration_window = Tk()
registration_window.geometry("400x400")
registration_window.title("Sign up")
registration_window.config(bg="sky blue")

firebase = firebase.FirebaseApplication("https://whitehatjr-pro-adv-188-default-rtdb.firebaseio.com/", None)

def login(): 
    global login_username_entry
    global login_password_entry
    print("login function")
    user2 = login_username_entry.get()
    pass2 = login_password_entry.get()
    user_check = firebase.get("/", user2)
    print(user_check)
    pass_check = firebase.get("/", pass2)
    print(pass_check)
    if (user_check == None):
        messagebox.showerror("LOL", "I can't find your account lol")
    
def register(): 
    print("register function")
    messagebox.showinfo("lol", "I have made you an account. Just remember that I CAN SEE YOUR PASSWORD")
    user = username_entry.get()
    password = password_entry.get()
    firebase.put("/", user, password)
    
def login_window():
    global login_username_entry
    global login_password_entry
    login_window = Tk()
    login_window.geometry("400x400")
    login_window.title("Sign in")
    login_window.config(bg="sky blue")
    
    log_heading_label = Label(login_window, text="Log In" , font = 'arial 18 bold', bg="sky blue", fg="white")
    log_heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username : " , font = 'arial 13', bg="sky blue", fg="white")
    login_username_label.place(relx=0.3,rely=0.4, anchor=CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password : " , font = 'arial 13', bg="sky blue", fg="white")
    login_password_label.place(relx=0.3,rely=0.5, anchor=CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font = 'arial 13 bold' , command=login, bd=0, bg="light green", fg="white")
    btn_login.place(relx=0.5,rely=0.65, anchor=CENTER)
    
    login_window.mainloop()
    
    
heading_label = Label(registration_window, text="Register" , font = 'arial 18 bold', bg="sky blue", fg="white")
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

username_label = Label(registration_window, text="Username : " , font = 'arial 13', bg="sky blue", fg="white")
username_label.place(relx=0.3,rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password :  " , font = 'arial 13', bg="sky blue", fg="white")
password_label.place(relx=0.3,rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font = 'arial 13 bold' ,command=register, bd=0, bg="light green", fg="white", padx=10)
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Sign In" , font = 'arial 10 bold' ,  command=login_window, bd=0, bg="light green", fg="white")
btn_login_window.place(relx=0.9,rely=0.06, anchor=CENTER)

alredy_a_user = Label(registration_window, text="Already a user?", bg="sky blue", fg="white", font = 'arial 13 bold')
alredy_a_user.place(relx=0.5, rely=0.03)

registration_window.mainloop()