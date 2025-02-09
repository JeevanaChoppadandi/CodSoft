import tkinter as tk
from tkinter import messagebox
import random

# Game logic
def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# GUI setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("300x400")

tk.Label(root, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14)).pack(pady=10)

# Creating round buttons using an image trick
button_style = {"font": ("Arial", 14), "bd": 2, "relief": "ridge", "width": 10, "height": 2}

rock_btn = tk.Button(root, text="Rock", command=lambda: play("Rock"), **button_style)
rock_btn.pack(pady=10)

paper_btn = tk.Button(root, text="Paper", command=lambda: play("Paper"), **button_style)
paper_btn.pack(pady=10)

scissors_btn = tk.Button(root, text="Scissors", command=lambda: play("Scissors"), **button_style)
scissors_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), pady=20)
result_label.pack()
root.mainloop()