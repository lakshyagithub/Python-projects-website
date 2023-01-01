#Libraries
from tkinter import *
from PIL import Image, ImageTk
import random

#Window properties
root = Tk()
root.title("endless dice game")
root.geometry("600x400")
root.configure(background="Pink")

#Dice
Dice_image = ImageTk.PhotoImage(Image.open ("dice.jpg"))

#Labels
player1 = Label(root, text="Player 1", bg="Cyan")
player2 = Label(root, text="Player 2", bg="Cyan")
player1_score = Label(root, bg="sky blue", fg="white")
player2_score = Label(root, bg="sky blue", fg="white")
score_of_player = Label(root, bg="Orangered", fg="white")

#Placing
player1.place(relx=0.2, rely=0.3, anchor=CENTER)
player2.place(relx=0.8, rely=0.3, anchor=CENTER)
player1_score.place(relx=0.2, rely=0.4, anchor=CENTER)
player2_score.place(relx=0.8, rely=0.4, anchor=CENTER)
score_of_player.place(relx=0.5, rely=0.5, anchor=CENTER)

#functions for rolling the dice
player1_s = 0
player2_s = 0
def player1_s_function():
	global player1_s
	r = random.randint(1,6)
	score_of_player["text"] = "player 1 score: " + str(r)
	player1_s = player1_s + r
	player1_score["text"] = str(player1_s)

def player2_s_function():
	global player2_s
	r = random.randint(1,6)
	score_of_player["text"] = "player 2 score: " + str(r)
	player2_s = player2_s + r
	player2_score["text"] = str(player2_s)

btn1 = Button(root, image=Dice_image, command=player1_s_function, bd=0)
btn2 = Button(root, image=Dice_image, command=player2_s_function, bd=0)

btn1.place(relx=0.2, rely=0.6, anchor=CENTER)
btn2.place(relx=0.8, rely=0.6, anchor=CENTER)
root.mainloop()