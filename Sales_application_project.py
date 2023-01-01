from tkinter import *

root = Tk()
root.geometry("700x400")
root.title("Sales application")
root.configure(background="light green")

month1 = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (100, 200, 300, 400, 500, 1000, 2000, 3000, 4000, 3000, 100, 10)

max_profit = max(profits)
min_profit = min(profits)

max_profit_index = profits.index(max_profit)
min_profit_index = profits.index(min_profit)

#print("Max profit index: " + str(max_profit_index) + ", Min profit index: " + str(min_profit_index))
max_month = month1[max_profit_index]
min_month = month1[min_profit_index]

#print("Max profit made in: " + max_month + ". Profit made: " + str(max_profit))
#print("Min profit made in: " + min_month + ". Profit made: " + str(min_profit))

month1_label = Label(root, text="Months:" + str(month1))
profits_label = Label(root, text="Profits:" + str(profits))
max_profit_label = Label(root, text="Max Profit:")
min_profit_label = Label(root, text="Min Profit:")

def update_max():
    max_profit_label["text"] += str(max_profit) + " in the month of: " + max_month

def update_min():
    min_profit_label["text"] += str(min_profit) + " in the month of: " + min_month

btn_min = Button(root, text="Show min profiable month", command=update_min, bg="sky blue", fg="white", bd=0)
btn_max = Button(root, text="Show max profiable month", command=update_max, bg="sky blue", fg="white", bd=0)

month1_label.place(relx=0.5, rely=0.3, anchor=CENTER)
profits_label.place(relx=0.5, rely=0.4, anchor=CENTER)
btn_min.place(relx=0.5, rely=0.5, anchor=CENTER)
min_profit_label.place(relx=0.5, rely=0.6, anchor=CENTER)
btn_max.place(relx=0.5, rely=0.7, anchor=CENTER)
max_profit_label.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()