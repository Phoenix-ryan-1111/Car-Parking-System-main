import A0MyModules as m
import tkinter as tk
from tkinter import *
from tkinter import ttk
def Parkinginsert():
    root = tk.Toplevel()
    root.title('Parking status')

    def Insert():
        Parking_id = l2.get()
        Floor = l4.get()
        Total = l7.get()
        if len(Parking_id) == 0 or len(Floor) == 0 or len(Total) == 0:
            mssg = "You haven't filled all the required details."
            l5.config(text=mssg)
        elif not Parking_id.isdigit():
            mssg = "Enter a valid Parking ID "
            l5.config(text=mssg)
        elif not Total.isdigit():
            mssg = "Enter a valid number of Parkings "
            l5.config(text=mssg)
        elif not Floor.isalpha():
            mssg = "Enter a valid Floor"
            l5.config(text=mssg)
        else: 
            query = f"insert into parking values ('{Parking_id}', '{Floor}', '{Total}' );"
            e=m.SqlConnectivity_Insert(query)
            if type(e) is not int:
                mssg = "Error: Place ID already exists." 
            else:
                mssg = "Successful"
            l5.config(text=mssg)


    ttk.Label(root, text='Insert Parking', font=("Arial", 20, "bold")).grid(row=0, column=1, columnspan=2,  pady=10)

    l1 = ttk.Label(root, text="Parking Id")
    l1.grid(row=1, column=1,  padx=10, pady=10,  ipadx=5, ipady=5)
    l2 = ttk.Entry(root)
    l2.grid(row=1, column=2,  padx=10, pady=10, ipadx=5, ipady=5)

    l3 = ttk.Label(root, text="Floor")
    l3.grid(row=2, column=1,  padx=10, pady=10, ipadx=5, ipady=5)
    l4 = ttk.Entry(root)
    l4.grid(row=2, column=2,  padx=10, pady=10, ipadx=5, ipady=5)


    l6 = ttk.Label(root, text="Total Parking Space")
    l6.grid(row=3, column=1,  padx=10, pady=10, ipadx=5, ipady=5)
    l7 = ttk.Entry(root)
    l7.grid(row=3, column=2,  padx=10, pady=10, ipadx=5, ipady=5)

    button = ttk.Button(root, text="Insert", command=Insert)
    button.grid(row=5, column=1, columnspan = 2, padx=(40, 20), pady=10)



    l5 = ttk.Label(root, text=" ", font=("Arial", 10, "bold"))
    l5.grid(row=6, column=1, columnspan=2,)

    root.mainloop()


