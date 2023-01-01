# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:23:37 2022

@author: laksh
"""

#First Class
class class1:
    
    def __init__(self):
        name1 = input("Hello. What is your name? \n")
        print("Hello,", name1)

#object_class1 = class1()

#Second class
class class2:
    def __init__(self, name2):
        print("This is", name2)
        
#name2 = input("Enter name any object name: \n")
#object_class2 = class2(name2)

#Third object
class class3:
    def __init__(self, name, dob, age, id_number):
        self.person_name = name
        self.person_dob = dob
        self.person_age = age
        self.person_id_number = id_number
    def add_person(self):
        print("Name:", self.person_name)
        print("DOB:", self.person_dob)
        print("Age:", str(self.person_age))
        print("ID number:", self.person_id_number)
        print("Done")

name_input = input("What is your name? \n")
dob_input = input("What is your DOB? \n")
age_input = input("What is your age? \n")
ID_input = input("What is your ID? \n")

object_class3 = class3(name_input, dob_input, age_input, ID_input)
object_class3.add_person()