import A0MyModules as m
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
def VEhicleShow():
    root = tk.Toplevel()

    root.title("Vehicle List")

    def searchError():
        messagebox.showinfo("ERROR!!!", " ERROR!!!." )

    def Search():
        search_Text = l2.get()
        if len(search_Text) == 0:
            searchError()
        else:
            top1 = Toplevel(root)   ## creates a new window
            top1.title("Searched Record")
            
            columns = ('Vehicle_Num', 'Type', 'Color', 'Company') 
            tv = ttk.Treeview(top1, columns=columns)
            tv.column('#0', width=5, stretch=False)           ## represents the parent
            tv.column('Vehicle_Num', anchor=CENTER, width=80)
            tv.column('Type', anchor=CENTER, width=80)
            tv.column('Color', anchor=CENTER, width=80)
            tv.column('Company', anchor=CENTER, width=80)

            for col in columns:
                tv.heading(col, text=col)

            query = f"select * from vehicle where Vehicle_Num= '{search_Text}';"
            result = m.SqlConnectivity_Show_Search_DashboardStatus_TotalParking1(query)

            for row in result:
                tv.insert(parent='', index='end', values=row )  ## index will show all till end

            tv.grid()




    l1 = ttk.Label(root, text="Vehicle Num:", font=("Arial", 10, "bold"))
    l1.grid(row=0, column=0, columnspan=2)
    l2 = ttk.Entry(root)
    l2.grid(row=0, column=2,sticky=tk.W+tk.E)
    button = ttk.Button(root, text="Search", command=Search)
    button.grid(row=0, column=3)


    columns = ('Vehicle_Num', 'Type', 'Color', 'Company') 
    tv = ttk.Treeview(root, columns=columns)
    tv.column('#0', width=5, stretch=False)           ## represents the parent
    tv.column('Vehicle_Num', anchor=CENTER, width=80)
    tv.column('Type', anchor=CENTER, width=80)
    tv.column('Color', anchor=CENTER, width=80)
    tv.column('Company', anchor=CENTER, width=80)


    for col in columns:
        tv.heading(col, text=col)
        
    #  data from the database
    query = "SELECT * FROM vehicle"
    result = m.SqlConnectivity_Show_Search_DashboardStatus_TotalParking1(query)

    # Insert data into the Treeview
    for row in result:
        tv.insert(parent='', index='end', values=row )  ## index will show all till end

    tv.grid(row=1, column=0, columnspan=4)


    root.mainloop()