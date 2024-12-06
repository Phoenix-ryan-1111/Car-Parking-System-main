import A0MyModules as m
import tkinter as tk
from tkinter import *
from tkinter import ttk

def DashBoardFloorStatus():
    root = tk.Toplevel()
    root.title('Parking status')


    def Check(*args):      ## *args = with this we dont need button to start this function it will start automatically see second last line of code
        selected_status = plot_status.get()
        # print(selected_status)

        if selected_status:
            query1 = f"select Total from parking where Floor = '{selected_status}' ;"
            query2 = f"select count(Available) from booking where floor  = '{selected_status}';"
            query3 = f"SELECT (select Total from parking where Floor = '{selected_status}') - (select count(Available) from booking where floor  = '{selected_status}');"
        else:
            mssg = "Invalid plot status"
            l5.config(text=mssg)

        result1 = m.SqlConnectivity_Show_Search_DashboardStatus_TotalParking1(query1)
        result2 = m.SqlConnectivity_Show_Search_DashboardStatus_TotalParking1(query2)
        result3 = m.SqlConnectivity_Show_Search_DashboardStatus_TotalParking1(query3)
        if result1 and result2 and result3: 
            Total, Available, Booked = result1[0], result2[0], result3[0]
            l2.config(text=Total)
            l7.config(text=Available)
            l4.config(text=Booked)
        


    plot_status = StringVar()
    ttk.Label(root, text='Plot Status', font=("Arial", 20, "bold")).grid(row=0, column=1, columnspan=2,  pady=10)
    l0 = ttk.Label(root, text="Plot Status")
    l0.grid(row=1, column=1, padx=10, pady=10)
    plot_status = StringVar()
    query4 = "select Floor from parking"
    result4 = m.SqlConnectivity_Show_Search_DashboardStatus_TotalParking1(query4)
    # print(result4)   ## will give tupple ## no use here 
    default_value = result4[0][0]  # Choose the desired default value from result4 ## [0][0] to get value from tupple
    status_dropdown = ttk.OptionMenu(root, plot_status, default_value, *result4) ## *result4, we are unpacking the elements of result4 and passing them as separate arguments.
    status_dropdown.grid(row=1, column=2, padx=10, pady=10)



    l1 = ttk.Label(root, text="Total")
    l1.grid(row=2, column=1, padx=10, pady=10)
    l2 = ttk.Label(root, text="")
    l2.grid(row=2, column=2,  padx=10, pady=10)

    l3 = ttk.Label(root, text="Available")
    l3.grid(row=3, column=1, padx=10, pady=10)
    l4 = ttk.Label(root, text="")
    l4.grid(row=3, column=2,  padx=10, pady=10)

    l6 = ttk.Label(root, text="Booked")
    l6.grid(row=4, column=1, padx=10, pady=10)
    l7 = ttk.Label(root, text="")
    l7.grid(row=4, column=2,  padx=10, pady=10)

    l5 = ttk.Label(root, text=" ", font=("Arial", 10, "bold"))
    l5.grid(row=6, column=1, columnspan=2)
    plot_status.trace("w", Check) ##*args == with this 
    Check() ## when user opens default results will be shown

    root.mainloop()
