import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        pass

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Task Entry
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(app, text="Add Task",bg="brown", command=add_task)
add_button.pack()

# Task List
task_list = tk.Listbox(app, width=40, height=10)
task_list.pack()

# Remove Task Button
remove_button = tk.Button(app, text="Remove Task",bg="brown",command=remove_task)
remove_button.pack()

# Start the application
app.mainloop()
