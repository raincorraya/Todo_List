from tkinter import END
import tkinter as tk
from tkinter import Listbox, Scrollbar, Button, PhotoImage

task_list = []

def addTask():
    task = task_entry.get()
    task_entry.delete(0, END)  # Now END is defined
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def deleteTask():
    selected_index = listbox.curselection()  # Get the index of the selected item
    if selected_index:  # Check if an item is selected
        index = int(selected_index[0])  # Convert tuple to integer
        task = listbox.get(index)  # Get the task from the listbox
        listbox.delete(index)  # Remove the task from the listbox
        task_list.remove(task)  # Remove the task from the task_list
        with open("tasklist.txt", "w") as taskfile:
            taskfile.write('\n'.join(task_list))  # Rewrite the task list to the file

def openTaskFile():
    try:
        global task_list
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
            for task in tasks:
                if task.strip():  # Check if task is not empty or whitespace
                    task_list.append(task.strip())
                    listbox.insert(tk.END, task.strip())  # Assuming 'listbox' is your tkinter Listbox widget
    except FileNotFoundError:  # Handle file not found error
        with open("tasklist.txt", "w") as file:
            pass  # Create an empty file if it doesn't exist

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x650+400+100")  # Set window size and position
root.resizable(False, False)  # Disable resizing

# Load and set the application icon
image_icon = PhotoImage(file=r"C:/Users/User/Pictures/x/task.png")
root.iconphoto(False, image_icon)
root.config(bg="Sky blue")
# Load images for top bar and dock
top_image = PhotoImage(file=r"C:/Users/User/Pictures/x/topbar (1).png")
dock_image = PhotoImage(file=r"C:/Users/User/Pictures/x/dock.png")
note_image = PhotoImage(file=r"C:/Users/User/Pictures/x/task.png")

# Top bar
tk.Label(root, image=top_image,bg="sky blue").pack()

# Dock
tk.Label(root, image=dock_image, bg="#32405b").place(x=30, y=25)

# Note image
tk.Label(root, image=note_image, bg="#32405b").place(x=340, y=25)

# Heading
heading_label = tk.Label(root, text="Every Task Hub", font="arial 20 bold", fg="white", bg="#32405b")
heading_label.place(x=90, y=20)

# Main Frame
frame = tk.Frame(root, width=400, height=50, bg="black")
frame.place(x=0, y=180)

# Task Entry
task_entry = tk.Entry(frame, width=18, font="arial 20", bd=0)
task_entry.place(x=10, y=7)
task_entry.focus()

# Add Button
button = tk.Button(frame, text="Add", font="arial 20 bold", width=6, bg="#32405b", fg="white", bd=0,command=addTask)
button.place(x=290, y=0)

# Listbox Frame
frame1 = tk.Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))

# Listbox
listbox = Listbox(frame1, font=('arial', 12), width=40, height=16, bg="#32405b", fg="white", cursor='hand2', selectbackground="gray", selectforeground="black")
listbox.pack(side=tk.LEFT, fill=tk.BOTH, padx=2)

# Scrollbar
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Delete Button
delete_icon = PhotoImage(file=r"C:\Users\User\Pictures\Saved Pictures\VAI.png")
delete_button = Button(root, image=delete_icon, bd=0, command=deleteTask)
delete_button.pack(side=tk.BOTTOM, pady=16)

# Call the function to populate task_list and create the file if needed
openTaskFile()

root.mainloop()
