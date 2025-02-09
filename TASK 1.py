import tkinter as tk
from tkinter import messagebox
import os

# File to save tasks
TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for task in file.readlines():
                task_list.insert(tk.END, task.strip())

# Save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        tasks = task_list.get(0, tk.END)
        file.write("\n".join(tasks))

# Add task
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Delete task
def delete_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Mark task as completed
def complete_task():
    try:
        selected_task = task_list.curselection()[0]
        task = task_list.get(selected_task)
        task_list.delete(selected_task)
        task_list.insert(tk.END, f"✔ {task}")  # Mark completed
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to complete.")

# GUI Setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

tk.Label(root, text="To-Do List", font=("Arial", 18, "bold")).pack(pady=10)

task_entry = tk.Entry(root, font=("Arial", 14), width=30)
task_entry.pack(pady=5)

tk.Button(root, text="Add Task", font=("Arial", 12), command=add_task).pack(pady=5)
tk.Button(root, text="Delete Task", font=("Arial", 12), command=delete_task).pack(pady=5)
tk.Button(root, text="Mark Completed", font=("Arial", 12), command=complete_task).pack(pady=5)

task_list = tk.Listbox(root, font=("Arial", 12), width=40, height=15)
task_list.pack(pady=10)
load_tasks()
root.mainloop()
