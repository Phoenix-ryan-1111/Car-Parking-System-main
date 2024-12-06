from JWelcomepage import *
import A0MyModules as m
import tkinter as tk
from tkinter import *
from tkinter import ttk   ## tkinter is pre defined jisma sa ttk nikal diya
from tkinter import messagebox 


def Login():
    
    root = tk.Toplevel()  
    root.attributes("-fullscreen", True)    ## for new Window
    center_frame = Frame(root)
    center_frame.pack(expand=True)

    def Incomplete_BOX():
        messagebox.showinfo("ERROR!!!", "You haven't filled all the required details." )
    def success_box():
        messagebox.showinfo("Successful", "Successful")
    def ERROR_BOX():
        messagebox.showinfo("Error!!!", "No Record Found")

    def Login():
        Username = l2.get()
        Password = l4.get()

        if len(Username) == 0 or len(Password) == 0:
            Incomplete_BOX()
        else:
            query1 = f"select Username, Password from login where Username = '{Username}' and password='{Password}';"
            result1=m.SqlConnectivity_Login(query1)
            # print(result1[0])
            if result1:
                Welcome()
            else:
                ERROR_BOX()  # Display success message box

    def Exit():
        root.destroy()


    l0=ttk.Label(center_frame, text='Login', font=("Arial", 20, "bold"), foreground='Gray')
    l0.grid(row= 0, column=0, columnspan=4, padx=10, pady=10, ipadx=5,ipady=5) 


    l1 = ttk.Label(center_frame, text="Enter Username")
    l1.grid(row=1, column=1)
    l2 = ttk.Entry(center_frame)
    l2.grid(row=1, column=2, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)

    l3 = ttk.Label(center_frame, text="Enter Password")
    l3.grid(row=2, column=1)
    l4 = ttk.Entry(center_frame)
    l4.grid(row=2, column=2, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)



    button = ttk.Button(center_frame, text="Login", command=Login)
    button.grid(row=3, column=1, padx=30, pady=30, ipadx=5, ipady=5)
    button = ttk.Button(center_frame, text="Exit",  command=Exit)
    button.grid(row=3, column=2, columnspan=2, padx=10, pady=30, ipadx=5, ipady=5)


    root.mainloop() 
