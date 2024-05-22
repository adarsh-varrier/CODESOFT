import tkinter as tk
import random


def play():
    choices=['Rock','Paper','Scissors']
    computer_choice=random.choice(choices)
    user_choice=user_var.get()

    #determine Winner
    if user_choice == computer_choice:
        result_var.set("ITS TIE!!!")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
            (user_choice == 'Paper' and computer_choice == 'Rock') or \
            (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result_var.set("***YOU WIN!***")
    else:
        result_var.set("[: YOU LOST! :(")

    computer_choice_var.set("Computer's Choise:-" + computer_choice)

#Create GuI

window= tk.Tk()
window.title("Rock-Paper-Scissors GAME")
window.config(bg="lightgreen")

#Creating User Choice DropDown

choices = ['Rock', 'Paper', 'Scissors']
user_var=tk.StringVar()
user_var.set(choices[0])
user_dropdown = tk.OptionMenu(window, user_var, *choices)
user_dropdown.place(x=680,y=180)
user_dropdown.config(bg="lightblue", fg="black", activebackground="blue", activeforeground="white")
user_dropdown.config(width=20, height=2)

#play button
play_button=tk.Button(window,text='Play',command=play,bg='red')
play_button.place(x=700,y=500)
play_button.config(font=("Helvetica", 16))
play_button.config(width=10, height=2)

# Create label to display computer's choice and result
computer_choice_var = tk.StringVar()
result_var = tk.StringVar()

computer_choice_label = tk.Label(window, textvariable= computer_choice_var, font=("Helvetica"), bg="yellow")
computer_choice_label.pack(padx=20,pady=350)
computer_choice_label.config(width=30,height=2)
result_label = tk.Label(window, textvariable=result_var,font=("Helvetica"), bg="pink")
result_label.place(x=20,y=400)
result_label.config(width=30,height=4)

computer_choice_label.pack()
result_label.pack(side=tk.BOTTOM, pady=10)

# Start the GUI
window.mainloop()




