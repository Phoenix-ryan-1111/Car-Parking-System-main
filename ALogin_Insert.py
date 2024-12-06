# import A0LoginMyModules as m
# import tkinter as tk
# from tkinter import *
# from tkinter import ttk   ## tkinter is pre defined jisma sa ttk nikal diya
# from tkinter import messagebox 
# root = tk.Tk()

# def Incomplete_BOX():
#     messagebox.showinfo("ERROR!!!", "You haven't filled all the required details." )
# def success_box():
#     messagebox.showinfo("Successful", "Successful")
# def ERROR_BOX():
#     messagebox.showinfo("Error!!!", "Error: Place ID already exists.")

# def Login():
#     Username = l2.get()
#     Password = l4.get()

#     if len(Username) == 0 or len(Password) == 0:
#         Incomplete_BOX()
#     else:
#         query = f"insert into login values ('{Username}', '{Password}')"
#         e=m.SqlConnectivity_Insert(query)
#         if e:
#             ERROR_BOX()
#         else:
#             success_box()  # Display success message box

# def Exit():
#     root.destroy()


# l0=ttk.Label(root, text='Login', font=("Arial", 20, "bold"))
# l0.grid(row= 0, column=0, columnspan=4, padx=10, pady=10, ipadx=5,ipady=5) 


# l1 = ttk.Label(root, text="Enter Username")
# l1.grid(row=1, column=1)
# l2 = ttk.Entry(root)
# l2.grid(row=1, column=2, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)

# l3 = ttk.Label(root, text="Enter Password")
# l3.grid(row=2, column=1)
# l4 = ttk.Entry(root)
# l4.grid(row=2, column=2, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)



# button = ttk.Button(root, text="Insert", command=Login)
# button.grid(row=3, column=1, padx=30, pady=10, ipadx=5, ipady=5)
# button = ttk.Button(root, text="Exit",  command=Exit)
# button.grid(row=3, column=2, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)


# root.mainloop() 
