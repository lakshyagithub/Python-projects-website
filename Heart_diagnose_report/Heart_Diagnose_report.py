from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x500")
root.title("Heart Diagnose Report.")
icon_image = PhotoImage(file="Icon.png")
root.iconphoto(False, icon_image)
root.configure(background="sky blue")

#Question 1 (The first question)
question1_radiobutton_value = StringVar(value="0")

Question1 = Label(root, text="Do you experience shortness of breath during routine activities?")
Question1.pack()
question1_r1 = Radiobutton(root, text="Yes", variable=question1_radiobutton_value, value="Yes")
question1_r1.pack()
question1_r2 = Radiobutton(root, text="No", variable=question1_radiobutton_value, value="No")
question1_r2.pack()

#Question 2
question2_radiobutton_value = StringVar(value="0")

Question2 = Label(root, text="Do you have sweling in the feet/ankles/legs (shoes feel tighter) or abdomen?")
Question2.pack()
question2_r1 = Radiobutton(root, text="Yes", variable=question2_radiobutton_value, value="Yes")
question2_r1.pack()
question2_r2 = Radiobutton(root, text="No", variable=question2_radiobutton_value, value="No")
question2_r2.pack()

#Question 3
question3_radiobutton_value = StringVar(value="0")

Question3 = Label(root, text="Do you feel any pain/symtomps for loof of memory?")
Question3.pack()
question3_r1 = Radiobutton(root, text="Yes", variable=question3_radiobutton_value, value="Yes")
question3_r1.pack()
question3_r2 = Radiobutton(root, text="No", variable=question3_radiobutton_value, value="No")
question3_r2.pack()

#Question 4
question4_radiobutton_value = StringVar(value="0")

Question4 = Label(root, text="Do you feel shortness of breath slowing down?")
Question4.pack()
question4_r1 = Radiobutton(root, text="Yes", variable=question4_radiobutton_value, value="Yes")
question4_r1.pack()
question4_r2 = Radiobutton(root, text="No", variable=question4_radiobutton_value, value="No")
question4_r2.pack()

#Question 5 (The last question)
question5_radiobutton_value = StringVar(value="0")

Question5 = Label(root, text="Is it okay now?")
Question5.pack()
question5_r1 = Radiobutton(root, text="Yes", variable=question5_radiobutton_value, value="Yes")
question5_r1.pack()
question5_r2 = Radiobutton(root, text="No", variable=question5_radiobutton_value, value="No")
question5_r2.pack()

def Check():
  score = 0
  
  global question1_radiobutton_value
  global question2_radiobutton_value
  global question3_radiobutton_value
  global question4_radiobutton_value
  global question5_radiobutton_value
  
  if question1_radiobutton_value.get() == "Yes":
    score = score+10
    print(score)
  if question2_radiobutton_value.get() == "Yes":
    score = score+10
    print(score)
  if question3_radiobutton_value.get() == "Yes":
    score = score+10
    print(score)
  if question4_radiobutton_value.get() == "Yes":
    score = score+10
    print(score)
  if question5_radiobutton_value.get() == "Yes":
    score = score+10
    print(score)

  if score <= 10:
    messagebox.showinfo("Report", "You don't need to visit a doctor")
  elif score > 10 and score <= 30:
    messagebox.showwarning("Report", "You might perhaps have to visit a doctor")
  else:
    messagebox.showerror("Report", "Visit the doctor ASAP!")
  

btn = Button(root, text="Submit", command=Check)
btn.pack()

root.mainloop()
