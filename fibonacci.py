from tkinter import *

root = Tk()

root.title("Fibonacci")
root.geometry("400x400")

label_series = Label(root, text="Fibonacci series")
label_flower = Label(root)
label_spiral = Label(root)

def fibonacci():
    num = 10
    first_no = 1
    second_no = 0
    sum = 1
    counter = 0
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        sum = first_no + second_no
        
    label_flower["text"] = "Flower is still blooming"
    label_spiral["text"] = "Sprials in the right direction are " + " and sprials in the left direction are " + str(second_no) + ".\n Total spirals are " + str(sum)
    
btn = Button(root, text="Show Fibonacci series", command=fibonacci)
btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()
root.mainloop()