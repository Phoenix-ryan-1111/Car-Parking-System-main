from ALogin import *
import tkinter as tk
import mysql.connector
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title('Welcome to Parking System')
# root.geometry('500x300')
# Make the window full screen
root.attributes("-fullscreen", True)
# Frame to center the content

## Frame to center the content
center_frame = Frame(root)
center_frame.pack(expand=True)


def Start():
    Login()
def Exit():
    root.destroy()

# Welcome message
welcome_label = ttk.Label(center_frame, text="Welcome to Parking System", font=('Helvetica', 20), foreground='Gray')
welcome_label.pack(pady=50)

# Start button
button = ttk.Button(center_frame, text="Start", command=Start)
button.pack(pady=20, ipadx=50, ipady=10)


button = ttk.Button(center_frame, text="Exit", command=Exit)
button.pack(pady=20, ipadx=50, ipady=10)


root.mainloop()


