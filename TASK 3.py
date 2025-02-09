import tkinter as tk
from tkinter import messagebox
import random
import string

# Generate password function
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4!")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except ValueError:
        messagebox.showwarning("Warning", "Please enter a valid number!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

tk.Label(root, text="Password Generator", font=("Arial", 18, "bold")).pack(pady=10)

tk.Label(root, text="Enter Password Length:", font=("Arial", 12)).pack()
length_entry = tk.Entry(root, font=("Arial", 14))
length_entry.pack(pady=5)

tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password).pack(pady=5)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, font=("Arial", 14), state="readonly", width=30)
password_entry.pack(pady=5)
root.mainloop()