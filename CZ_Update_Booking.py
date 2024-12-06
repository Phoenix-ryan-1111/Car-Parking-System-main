# dont make vehicle update bec isme saara data customer table sa ayaga so agr kuch bhi galat hua sara database ka tables foreign keys sa attach honge agr vehicle update krr diya toh Customer table ma bhi vehicle update krna padaga jo ki saara code aak dum hila ka rakh dega saar jgah change karna hoga so leave it isse acha entry delete kro and saara duabra sa shuru ho jayaga system vahi user dubara sa entry karo


import A0MyModules as m
import tkinter as tk
from tkinter import *
from tkinter import ttk
def Booking_Update():
    root = tk.Toplevel()

    root.title("Update Records")
    def update_record():  ##function ka andr function banana sa we can use previous values
        Old_Booking_slot_Num = l9.get()
        Updated_Booking_slot_Num = l11.get()

        if len(Old_Booking_slot_Num) == 0 or len(Updated_Booking_slot_Num) == 0:
            mssg = "You haven't filled all the required details."
            l14.config(text=mssg)
        else:
            query1 = f"UPDATE booking SET Booking_slot_num = '{Updated_Booking_slot_Num}' WHERE Booking_slot_num = '{Old_Booking_slot_Num}';"
            query2 = f"UPDATE customer SET Booking_slot_num = '{Updated_Booking_slot_Num}' WHERE Booking_slot_num = '{Old_Booking_slot_Num}';"
            result1 = m.SqlConnectivity_Update_record1(query1)
            result2 = m.SqlConnectivity_Update_record1(query2)

            if result1 and result2:
                mssg = "Successful"
                l14.config(text=mssg)
            else:
                mssg = "There is no such ID"
                l14.config(text=mssg)  

    l8 = ttk.Label(root, text="Enter Your Existing Booking slot ")
    l8.grid(row=1, column=0, padx=10, pady=10)
    l9 = ttk.Entry(root)
    l9.grid(row=1, column=1, padx=10, pady=10)

    l10 = ttk.Label(root, text="Enter Updated Booking Slot ")
    l10.grid(row=2, column=0, padx=10, pady=10)
    l11 = ttk.Entry(root)
    l11.grid(row=2, column=1, padx=10, pady=10)



    button = ttk.Button(root, text="Update", command=update_record)
    button.grid(row=5, column =0, columnspan=2, padx=(5, 20), pady=10)

    l14 = ttk.Label(root, text=" ", font=("Arial", 10, "bold"))
    l14.grid(row=6, columnspan=2)


    root.mainloop()


