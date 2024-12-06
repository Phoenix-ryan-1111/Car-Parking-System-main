### on one click details of user when he is leaving will be deleted from customer table, vehicle table, parking table.
###Multi Delete



### change parking_id to bookingID know bec parking includes all floor systems...........
import A0MyModules as m
import tkinter as tk
from tkinter import *
from tkinter import ttk

def CustomerDElete():
    root = tk.Toplevel()

    root.title("Delete Records")
    def hide_auto_fill_button():
        # Hide the "Auto Fill" button
        button.grid_remove()
    def Auto_Fill():
        global l4  # Declare l4 as global variable
        global l6  # Declare l6 as global variable
        Cust_ID = l2.get()
        if len(Cust_ID) == 0:
            mssg = "You haven't filled all the required details."
            l7.config(text=mssg)
        else:
            l3 = ttk.Label(root, text="Booking Slot Num ")
            l3.grid(row=3, column=0, padx=10, pady=10)
            l4= ttk.Label(root, text="")
            l4.grid(row=3, column=1, padx=10, pady=10)

            l5 = ttk.Label(root, text="Vehicle Num")
            l5.grid(row=4, column=0, padx=10, pady=10)
            l6= ttk.Label(root, text="")
            l6.grid(row=4, column=1, padx=10, pady=10)
            query1 = f"SELECT Booking_Slot_Num FROM customer WHERE Cust_ID = '{Cust_ID}';"
            query2 = f"SELECT Vehicle_Num FROM customer WHERE Cust_ID = '{Cust_ID}';"
            result1 = m.Auto_Fill(query1)
            result2 = m.Auto_Fill(query2)
            print(result1)
            print(result2)
            if result1 and result2:
                Booking_Slot_Num , Vehicle_Num = result1[0], result2[0]  ## fetching 0 index bec ans is a tupple
                # l4.delete(0, END) 
                l4.config(text= Booking_Slot_Num )
                # l6.delete(0, END)
                l6.config(text= Vehicle_Num)
                hide_auto_fill_button()  # Hide the "Auto Fill" button
            else:
                mssg = "There is no such ID"
                l7.config(text=mssg)
            button = ttk.Button(root, text="Delete", command=delete_record)
            button.grid(row=5, column=0, columnspan=2, padx=(5, 20), pady=10)

    def delete_record():
        Cust_ID = l2.get()
        Booking_Slot_Num = l4.cget("text")     ## to get the text value
        Vehicle_Num = l6.cget("text")
        
        if len(Cust_ID) == 0:
            mssg = "You haven't filled all the required details."
            l7.config(text=mssg)
        else:
            query1 = f"DELETE FROM customer WHERE cust_id = '{Cust_ID}';"
            query2 = f"DELETE FROM Booking WHERE Booking_Slot_Num = '{Booking_Slot_Num}';"
            query3 = f"DELETE FROM vehicle WHERE Vehicle_Num = '{Vehicle_Num}';"
            result = m.SqlConnectivity_Delete_Record(query1)
            result = m.SqlConnectivity_Delete_Record(query2)
            result = m.SqlConnectivity_Delete_Record(query3)
            if result :
                mssg = "Record deleted successfully."
                l7.config(text=mssg)
            else:
                mssg = "There is no such ID."
                l7.config(text=mssg)
        

    l1 = ttk.Label(root, text="Enter Your Customer ID ")
    l1.grid(row=1, column=0, padx=10, pady=10)
    l2= ttk.Entry(root)
    l2.grid(row=1, column=1, padx=10, pady=10)
    button = ttk.Button(root, text="Auto Fill", command=Auto_Fill)
    button.grid(row=2, column=0, columnspan=2, padx=(5, 20), pady=10)

    l7 = ttk.Label(root, text=" ", font=("Arial", 10, "bold"))
    l7.grid(row=6, columnspan=2)


    root.mainloop()


