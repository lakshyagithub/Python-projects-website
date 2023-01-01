# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:53:17 2022

@author: laksh
"""

from tkinter import *
root = Tk()
root.title("Inheritance")
root.geometry("600x600")

label_name = Label(root, text="User Name : ")
label_name.place(relx=0.3,rely=0.2, anchor=CENTER)
entry_name = Entry(root)
entry_name.place(relx=0.6,rely=0.2, anchor=CENTER)
label_email = Label(root, text="Email id : ")
label_email.place(relx=0.3,rely=0.3, anchor=CENTER)
entry_email = Entry(root)
entry_email.place(relx=0.6,rely=0.3, anchor=CENTER)
label = Label(root)

dictionary = {}
class Users: 
        
    def addUser(key, value): 
         #access the dictionary variable inside the class
         global dictionary
         #pass parameter key as the index to the dictionary and inside it assign the parameter as value.
         dictionary[key] = value
         #update the text parameter of the label with variable dictionary.
         label["text"] = dictionary
        

class GetUsers(Users): 
        
    def getUser(self):
        #using get() function get the entry_name from the user and store it in variable username
        username = entry_name.get()
        #using the get() function get the email_id from the user and store it in variable email_id
        email_id = entry_email.get()
        #access the addUser function of the users class and inside it pass the parameters as username, email_id
        Users.addUser(username, email_id)

#Create a object of GetUsers class        
user = GetUsers()
btn = Button(root, text="Add user details", command=user.getUser)
btn.place(relx=0.5,rely=0.4, anchor=CENTER)
label.place(relx=0.5,rely=0.5, anchor=CENTER)
root.mainloop()