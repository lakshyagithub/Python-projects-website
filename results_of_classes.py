# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:16:09 2022

@author: laksh
"""

from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("PTM")

label_grade_one = Label(root)
label_grade_two = Label(root)
label_grade_three = Label(root)

class gradeone:
    def __init__(self, math, science):
        self.math = math
        self.science = science
    def percentage(self):
        total_marks = self.math + self.science
        total_marks_with_100 = total_marks * 100
        grade_1_percentage = total_marks / 200
        label_grade_one["text"] = grade_1_percentage

class gradetwo:
    def __init__(self, math, science):
        self.math = math
        self.science = science
    def percentage(self):
        total_marks = self.math + self.science
        total_marks_with_100 = total_marks * 100
        grade_2_percentage = total_marks / 200
        label_grade_two["text"] = grade_2_percentage
        
class gradethree:
    def __init__(self, math, science):
        self.math = math
        self.science = science
    def percentage(self):
        total_marks = self.math + self.science
        total_marks_with_100 = total_marks * 100
        grade_3_percentage = total_marks / 200
        label_grade_three["text"] = grade_3_percentage
        
call_grade_one = gradeone(40, 50)
call_grade_two = gradetwo(10, 20)
call_grade_three = gradethree(20, 40)
btn1 = Button(root, text="Grade 1", command=call_grade_one.percentage)
btn2 = Button(root, text="Grade 2", command=call_grade_two.percentage)
btn3 = Button(root, text="Grade 3", command=call_grade_three.percentage)

btn1.pack(padx=20, pady=10)
label_grade_one.pack(padx=20, pady=10)
btn2.pack(padx=20, pady=10)
label_grade_two.pack(padx=20, pady=10)
btn3.pack(padx=20, pady=10)
label_grade_three.pack(padx=20, pady=10)

root.mainloop()