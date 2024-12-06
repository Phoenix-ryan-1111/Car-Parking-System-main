import A0MyModules as m
import tkinter as tk
from tkinter import *
from tkinter import ttk

def Dashboardstatus():
    root = tk.Toplevel()
    # root.geometry('300x300')
    root.title('Parking status')

    def Check():
        l2 = ttk.Label(root, text="")
        l2.grid(row=1, column=2,  padx=10, pady=10)
        l4 = ttk.Label(root, text="")
        l4.grid(row=2, column=2,  padx=10, pady=10)
        l7 = ttk.Label(root, text="")
        l7.grid(row=3, column=2,  padx=10, pady=10)
        
        
        query1 = f"select sum(Total) from parking;"
        query2 = f"select sum(Booked) from Booking;"
        query3 = f"SELECT (SELECT SUM(Total) FROM parking) - (SELECT SUM(Booked) FROM Booking);"

        result1=m.SqlConnectivity_Show_Search_DashboardStatus_TotalParking1(query1)
        result2=m.SqlConnectivity_Show_Search_DashboardStatus_TotalParking1(query2)
        result3=m.SqlConnectivity_Show_Search_DashboardStatus_TotalParking1(query3)
        if result1 and result2 :
            Total, Booked,Available= result1[0], result2[0], result3[0]
            l2.config(text= Total)
            l7.config(text= Booked)
            l4.config(text= Available)
    


    ttk.Label(root, text='Status', font=("Arial", 20, "bold")).grid(row=0, column=1, columnspan=2,  pady=10)

    l1 = ttk.Label(root, text="Total")
    l1.grid(row=1, column=1,  padx=10, pady=10)

    l3 = ttk.Label(root, text="Available")
    l3.grid(row=2, column=1,  padx=10, pady=10)


    l6 = ttk.Label(root, text="Booked")
    l6.grid(row=3, column=1,  padx=10, pady=10)

    l5 = ttk.Label(root, text=" ", font=("Arial", 10, "bold"))
    l5.grid(row=6, column=1, columnspan=2,)

    Check()
    root.mainloop()


