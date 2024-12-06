import A0MyModules as m
import tkinter as tk
from tkinter import *
from tkinter import ttk
def ParkingUpdate():
    root = tk.Toplevel()

    root.title("Update Parking")
    ttk.Label(root, text='Parking Floors Update', font=("Arial", 20, "bold")).grid(row=0, column=0, columnspan=2,  pady=10)

    l8 = ttk.Label(root, text="Enter Your Existing Parking Id")
    l8.grid(row=1, column=0, padx=10, pady=10)
    l9 = ttk.Entry(root)
    l9.grid(row=1, column=1, padx=10, pady=10)

    l10 = ttk.Label(root, text="New Floor Name")
    l10.grid(row=2, column=0, padx=10, pady=10)
    l11 = ttk.Entry(root)
    l11.grid(row=2, column=1, padx=10, pady=10)

    l12 = ttk.Label(root, text="Total Parkings in that Floor")
    l12.grid(row=3, column=0, padx=10, pady=10)
    l13 = ttk.Entry(root)
    l13.grid(row=3, column=1, padx=10, pady=10)


    def update_record():  ##function ka andr function banana sa we can use previous values
        Parking_id = l9.get()
        Floor = l11.get()
        Total_Parkings = l13.get()

        if len(Parking_id) == 0 or len(Floor) == 0 or len(Total_Parkings) == 0:
            mssg = "You haven't filled all the required details."
            l14.config(text=mssg)
        elif not Total_Parkings.isdigit():
            mssg = "Enter a valid number of parking floors."
            l14.config(text=mssg)
        elif not Floor.isalpha():
            mssg = "Enter a valid Floor."
            l14.config(text=mssg)
        else:
            query1 = f"SELECT parking_id FROM parking WHERE Parking_ID = '{Parking_id}';"
            query2 = f"UPDATE parking SET Floor = '{Floor}', Total = '{Total_Parkings}' WHERE Parking_ID = '{Parking_id}';"
            result = m.SqlConnectivity_Update_record(query1, query2)
            if not result:
                mssg = "There is no such ID."
                l14.config(text=mssg)
            else:
                mssg = "Successful"
                l14.config(text=mssg)  

    button = ttk.Button(root, text="Update", command=update_record)
    button.grid(row=5, column =0, columnspan=2, padx=(5, 20), pady=10)

    l14 = ttk.Label(root, text=" ", font=("Arial", 10, "bold"))
    l14.grid(row=6, columnspan=2)


    root.mainloop()


