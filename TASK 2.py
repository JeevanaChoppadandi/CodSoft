import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    current_text = entry_var.get()
    if button_text == "=":
        try:
            result = eval(current_text)
            entry_var.set(result)
        except:
            messagebox.showerror("Error", "Invalid Input")
    elif button_text == "C":
        entry_var.set("")
    else:
        entry_var.set(current_text + button_text)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 18), justify="right", bd=10, relief="ridge")
entry.grid(row=0, column=0, columnspan=4)

# Button Layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

for r, row in enumerate(buttons, 1):
    for c, char in enumerate(row):
        btn = tk.Button(root, text=char, font=("Arial", 18), width=5, height=2,
                        command=lambda ch=char: on_click(ch))
        btn.grid(row=r,column=c)
root.mainloop()
    
       
                        