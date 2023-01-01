from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x550")
root.title("Question for Daisy's percentage to vist the doctor")

score1 = int()

#The begin of the longest EVER(For me) code but small and easy for me

#Question number 1
question1_radiobutton_value = StringVar(value="0")

Question1 = Label(root, text="Do you have Headache and sore throught?")
Question1.pack()
question1_r1 = Radiobutton(root, text="Yes", variable=question1_radiobutton_value, value="Yes")
question1_r1.pack()
question1_r2 = Radiobutton(root, text="No", variable=question1_radiobutton_value, value="No")
question1_r2.pack()

#Question number 2
question2_radiobutton_value = StringVar(value="0")

Question2 = Label(root, text="Is your body tempeture too HIGH?")
Question2.pack()
question2_r1 = Radiobutton(root, text="Yes", variable=question2_radiobutton_value, value="Yes")
question2_r1.pack()
question2_r2 = Radiobutton(root, text="No", variable=question2_radiobutton_value, value="No")
question2_r2.pack()

#Question number 3
question3_radiobutton_value = StringVar(value="0")

Question3 = Label(root, text="Do you have coronavirus?")
Question3.pack()
question3_r1 = Radiobutton(root, text="Yes", variable=question3_radiobutton_value, value="Yes")
question3_r1.pack()
question3_r2 = Radiobutton(root, text="No", variable=question3_radiobutton_value, value="No")
question3_r2.pack()

root.mainloop()