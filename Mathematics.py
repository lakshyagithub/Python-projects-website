from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Mathematics")

input_number = Entry(root)
Fibonacci_series = Label(root)
sum_label = Label(root)

def fibonacci():
    input_data=int(input_number.get())

    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    sum2 = 0

    while (counter <= input_data):
        Fibonacci_series["text"] = "Fibonacci series: " + str(sum2)
        counter = counter+1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum2 + sum
        sum_label["text"] += str(sum) + "  "

btn = Button(root, text="Show Fibonacci Series", command=fibonacci)
input_number.pack()
btn.pack()
Fibonacci_series.pack()
sum_label.pack()

root.mainloop()