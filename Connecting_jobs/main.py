from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import random
root = Tk()
root.geometry("900x500")
#----------------------------loading image------------ 
#load the logo image and store it in variable image.
image = ImageTk.PhotoImage(Image.open("image2.png")) 


place_image=Label(root)
#update the "image" property of the variable place_image
place_image["image"] = image
place_image.place(relx=0.7, rely=0.5,anchor=CENTER)



#----------------------------heading of application--------------
#set the font family of the text in label as per your choice of size 20 and make it bold and set the foreground color of the label
label = Label(root, text="Assigning Jobs", font=("times", 15, "bold"), fg="blue")

label.place(relx=0.01, rely=0.06,anchor=W)


#------------------Label for string Docter-------------
label_doctor=Label(root,text="Doctor : ")
#place the label label_doctor at 0.04 and 0.15 relx and rely values respectively and set anchor to center.
label_doctor.place(relx=0.04, rely=0.15, anchor=CENTER)


#------------------Label for string IT professional-------------
label_IT=Label(root,text="IT professional : ")
#place the label label_IT at 0.06 and 0.45 relx and rely values respectively and set anchor to center.
label_IT.place(relx=0.06, rely=0.45, anchor=CENTER)


#------------------Label for string "Chemical Engineer ------------
label_chemical=Label(root,text="Chemical Engineer : ")
#place the label label_chemical at 0.07 and 0.75 relx and rely values respectively and set anchor to center.
label_chemical.place(relx=0.07, rely=0.75, anchor=CENTER)

#---------------------entry elements--------------------------------
entry_doctor = Entry(root)
entry_doctor.place(relx=0.25, rely=0.15,anchor=CENTER)

entry_IT = Entry(root)
entry_IT.place(relx=0.25, rely=0.45,anchor=CENTER)

entry_chemical = Entry(root)
entry_chemical.place(relx=0.25, rely=0.75,anchor=CENTER)
#------------------------Labels selected--------------------------
label_selected_doctor=Label(root, font=("times",12,"bold"),fg="dark olive green")
label_selected_doctor.place(relx=0.01, rely=0.3,anchor=W)

label_selected_IT=Label(root,font=("times",12,"bold"),fg="dark olive green")
label_selected_IT.place(relx=0.01, rely=0.6,anchor=W)

label_selected_chemical=Label(root, font=("times",12,"bold"),fg="dark olive green")
label_selected_chemical.place(relx=0.01, rely=0.9,anchor=W)

class parent():
    def __init__(self):
        print("This is parent class")
        
    def doctor(doctor_name):
        hospital_list = ["Apex", "Apollo", "City Care", "Galaxy"]
        random_hospital = random.randint(0,3)
        label_selected_doctor['text'] = doctor_name+" has been allotted to "+hospital_list[random_hospital]
        
    def softwareEngineer(it_professional_name):
        IT_company_list = ["I code", "Web Access", "Dotcom Services", "ATOS"]
        random_IT_company = random.randint(0,3)
        label_selected_IT['text'] = it_professional_name+" has been allotted to "+IT_company_list[random_IT_company]
        
    def chemicalEngineer(chemical_engineer_name):
        company_list = ["Air Liquide", "BASF", "Albemarle Corporation", "DuPont"]
        random_company = random.randint(0,3)
        label_selected_chemical['text'] = chemical_engineer_name+" has been allotted to "+company_list[random_company]
        
class child1(parent):
    def __init__(self):
        print("This is child1 class")
    def getDoctor(self):
        name = entry_doctor.get()
        parent.doctor(name)
        
class child2(parent):
    def __init__(self):
        print("This is child2 class")
    def getIT(self):
        name = entry_IT.get()
        parent.softwareEngineer(name)
        
class child3(parent):
    def __init__(self):
        print("This is child3 class")
    def getChemical(self):
        name = entry_chemical.get()
        parent.chemicalEngineer(name)
        
obj1 = child1()
obj2 = child2() 
obj3 = child3()


btn_doctor = Button(root, text="Show the hospital allotted", command=obj1.getDoctor,bg="#1763A5", fg="white",relief = FLAT)

btn_doctor.place(relx=0.1, rely=0.23,anchor=CENTER)
btn_it = Button(root, text="Show the IT company allotted", command=obj2.getIT,bg="#1763A5", fg="white",relief = FLAT)

btn_it.place(relx=0.11, rely=0.53,anchor=CENTER)
btn_chemical = Button(root, text="Show the chemical company allotted", command=obj3.getChemical, bg="#1763A5", fg="white",relief = FLAT)

btn_chemical.place(relx=0.13, rely=0.83,anchor=CENTER)
root.mainloop()
