import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("To-Do List App")

# Task list to hold tasks in memory
tasks = []

# GUI Elements
task_listbox = tk.Listbox(root, width=50, height=15)     # creates a scrollable and selectable list of items
task_listbox.pack(pady=10)

entry = tk.Entry(root, width=40)    # text input for new tasks
entry.pack(pady=5)

def add_task_gui():
    """
    Adds a task entered in the input field to the task list and updates the task list.
    """
    task = entry.get().strip()     # retrieves the text entered from the input box
    if task:
        tasks.append(task)
        update_task_listbox()     # updates task list
        entry.delete(0, tk.END)    # clears entry box
    else:
        messagebox.showwarning("Task cannot be empty.")

def remove_task_gui():
    """
    Removes the selected task from the task list and updates the task list.
    """
    try:
        selected_task_index = task_listbox.curselection()[0]    # retrieves the selected task
        tasks.pop(selected_task_index)
        update_task_listbox()    # updates task list
    except IndexError:
        messagebox.showwarning("Please select a task to remove.")    # user did not select a task

def update_task_listbox():
    """
    Clears and repopulates the task list in the Listbox.
    """
    task_listbox.delete(0, tk.END)    # clears task list
    for task in tasks:    # repopulates task list
        task_listbox.insert(tk.END, task)

def load_tasks():
    """
    Loads tasks from the "tasks" file and updates the GUI.
    If the file is missing, initializes with an empty task list.
    """
    try:
        with open("tasks", "r") as file:
            content = file.read().strip()
            tasks.extend(task for task in content.split('--*!->') if task)
            update_task_listbox()
    except FileNotFoundError:
        tasks.clear()    # If the file doesn't exist, start with an empty task list

def save_tasks():
    """
    Saves the current tasks to the "tasks" file.
    Each task is serialized as a string followed by the delimiter "--*!->".
    """
    with open("tasks", "w") as file:
        for task in tasks:
            file.write(f"{task}--*!->")

# Add buttons
add_button = tk.Button(root, text="Add Task", command=add_task_gui)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task_gui)
remove_button.pack(pady=5)

# Load tasks when the app starts
load_tasks()

# Save tasks when the window is closed
root.protocol("WM_DELETE_WINDOW", save_tasks)

# Start the Tkinter main loop
root.mainloop()
