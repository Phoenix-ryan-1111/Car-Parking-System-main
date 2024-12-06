import A0MyModules as m
import tkinter as tk
from tkinter import *
from tkinter import ttk
def Parkingdelete():
    root = tk.Toplevel()
    root.title("Delete Parking")

    l1 = ttk.Label(root, text="Enter Parking ID You Want to delete")
    l1.grid(row=1, column=0, padx=10, pady=10)
    l2 = ttk.Entry(root)
    l2.grid(row=1, column=1, padx=10, pady=10)

    l3 = ttk.Label(root, text=" ", font=("Arial", 10, "bold"))
    l3.grid(row=2, columnspan=2)

    def delete_record():
        Parking_id = l2.get()

        if len(Parking_id) == 0:
            mssg = "You haven't filled the required details."
            l3.config(text=mssg)
        else:
            query = f"DELETE FROM parking WHERE Parking_ID = '{Parking_id}';"
            x = m.SqlConnectivity_Delete_Record(query)
            if x :
                mssg = "Record deleted successfully."
                l3.config(text=mssg)
            else:
                mssg = "There is no such ID."
                l3.config(text=mssg)

    button = ttk.Button(root, text="Delete", command=delete_record)
    button.grid(row=3, columnspan=2, padx=(5, 20), pady=10)

    root.mainloop()
