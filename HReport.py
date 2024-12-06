import A0MyModules as m
import tkinter as tk
from tkinter import *
from tkinter import ttk

def report():
    root = tk.Toplevel()
    root.title("Update Records")
    # Configure ttk style for the separator
    style = ttk.Style()
    style.configure("Horizontal.TSeparator", background="black", thickness=3)

    def auto_fill():
        Cust_ID = l.get()
        # making all variables global so that they can be accessed in further functions
        global l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15

        if len(Cust_ID) == 0:
            mssg = "You haven't filled all the required details."
            l16.config(text=mssg)
        else:
            l0 = ttk.Label(root, text="Booking Slot Number ")
            l0.grid(row=4, column=0, padx=5, pady=5)
            l0 = ttk.Entry(root)
            l0.grid(row=4, column=1, padx=5, pady=5)

            l1 = ttk.Label(root, text="Transaction ID")
            l1.grid(row=4, column=2, padx=5, pady=5)
            l1 = ttk.Entry(root)
            l1.grid(row=4, column=3, padx=5, pady=5)

            l2 = ttk.Label(root, text="Vehicle Number")
            l2.grid(row=4, column=4, padx=5, pady=5)
            l2 = ttk.Entry(root)
            l2.grid(row=4, column=5, padx=5, pady=5)

            l3 = ttk.Label(root, text="First Name")
            l3.grid(row=4, column=6, padx=5, pady=5)
            l3 = ttk.Entry(root)
            l3.grid(row=4, column=7, padx=5, pady=5)

            l4 = ttk.Label(root, text="Last Name")
            l4.grid(row=4, column=8, padx=5, pady=5)
            l4 = ttk.Entry(root)
            l4.grid(row=4, column=9, padx=5, pady=5)

            l5 = ttk.Label(root, text="Phone")
            l5.grid(row=4, column=10, padx=5, pady=5)
            l5 = ttk.Entry(root)
            l5.grid(row=4, column=11, padx=5, pady=5)

            l6 = ttk.Label(root, text="Address")
            l6.grid(row=4, column=12, padx=5, pady=5)
            l6 = ttk.Entry(root)
            l6.grid(row=4, column=13, padx=5, pady=5)
            # ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=5, columnspan=2, sticky="ew")

            l7 = ttk.Label(root, text="Floor ")
            l7.grid(row=6, column=0, padx=5, pady=5)
            l7 = ttk.Entry(root)
            l7.grid(row=6, column=1, padx=5, pady=5)
            # ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=7, columnspan=2, sticky="ew")

            l8 = ttk.Label(root, text="Type Of Vehicle")
            l8.grid(row=8, column=0, padx=5, pady=5)
            l8 = ttk.Entry(root)
            l8.grid(row=8, column=1, padx=5, pady=5)

            l9 = ttk.Label(root, text="Color")
            l9.grid(row=8, column=2, padx=5, pady=5)
            l9 = ttk.Entry(root)
            l9.grid(row=8, column=3, padx=5, pady=5)

            l10 = ttk.Label(root, text="Company")
            l10.grid(row=8, column=4, padx=5, pady=5)
            l10 = ttk.Entry(root)
            l10.grid(row=8, column=5, padx=5, pady=5)
            # ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=9, columnspan=2, sticky="ew")

            l11 = ttk.Label(root, text="Type Of Transaction")
            l11.grid(row=10, column=0, padx=5, pady=5)
            l11 = ttk.Entry(root)
            l11.grid(row=10, column=1, padx=5, pady=5)

            l12 = ttk.Label(root, text="Amount")
            l12.grid(row=10, column=2, padx=5, pady=5)
            l12 = ttk.Entry(root)
            l12.grid(row=10, column=3, padx=5, pady=5)

            l13 = ttk.Label(root, text="In Time")
            l13.grid(row=10, column=4, padx=5, pady=5)
            l13 = ttk.Entry(root)
            l13.grid(row=10, column=5, padx=5, pady=5)

            l14 = ttk.Label(root, text="Out Time")
            l14.grid(row=10, column=6, padx=5, pady=5)
            l14 = ttk.Entry(root)
            l14.grid(row=10, column=7, padx=5, pady=5)

            l15 = ttk.Label(root, text="Date")
            l15.grid(row=10, column=8, padx=5, pady=5)
            l15 = ttk.Entry(root)
            l15.grid(row=10, column=9, padx=5, pady=5)

            query1 = f"SELECT Booking_Slot_Num, Transaction_ID, Vehicle_Num, First_Name, Last_Name, Phone, Address FROM customer WHERE Cust_ID = '{Cust_ID}';"
            result1 = m.Auto_Fill(query1)
            print(result1[0])  ## shows it is working properly====== Very Very Imp
            print(result1[1])
            print(result1[2])
            query2 = f"SELECT Floor from booking WHERE Booking_Slot_Num = '{result1[0]}';"
            result2 = m.Auto_Fill(query2)
            print(result2[0])
            query3 = f"SELECT Type, Color, Company from vehicle WHERE Vehicle_Num = '{result1[2]}';"
            result3 = m.Auto_Fill(query3)
            print(result3[0])
            query4 = f"SELECT Type, Amount, In_Time, Out_Time, Date from transaction WHERE Transaction_ID = '{result1[1]}';"
            result4 = m.Auto_Fill(query4)

            if result1[0] and result1[1] and result1[2] and result1[3] and result1[4] and result1[5] and result1[6] and result2[0] and result3[0] and result3[1] and result3[2] and result4[0] and result4[1] and result4[2] and result4[3] and result4[4]:
                Booking_Slot_Num = result1[0]  # 0 will select first value from tuple # index starts with 0
                Transaction_ID = result1[1]  # 1 will select second value from tuple
                Vehicle_Num = result1[2]
                First_Name = result1[3]
                Last_Name = result1[4]
                Phone = result1[5]
                Address = result1[6]
                Floor = result2[0]
                Type = result3[0]
                Color = result3[1]
                Company = result3[2]
                Type_Transaction = result4[0]
                Amount = result4[1]
                In_Time = result4[2]
                Out_Time = result4[3]
                Date = result4[4]

                l0.insert(0, Booking_Slot_Num)
                l0.config(state='readonly')
                l1.insert(0, Transaction_ID)
                l1.config(state='readonly')
                l2.insert(0, Vehicle_Num)
                l2.config(state='readonly')
                l3.insert(0, First_Name)
                l3.config(state='readonly')
                l4.insert(0, Last_Name)
                l4.config(state='readonly')
                l5.insert(0, Phone)
                l5.config(state='readonly')
                l6.insert(0, Address)
                l6.config(state='readonly')
                l7.insert(0, Floor)
                l7.config(state='readonly')
                l8.insert(0, Type)
                l8.config(state='readonly')
                l9.insert(0, Color)
                l9.config(state='readonly')
                l10.insert(0, Company)
                l10.config(state='readonly')
                l11.insert(0, Type_Transaction)
                l11.config(state='readonly')
                l12.insert(0, Amount)
                l12.config(state='readonly')
                l13.insert(0, In_Time)
                l13.config(state='readonly')
                l14.insert(0, Out_Time)
                l14.config(state='readonly')
                l15.insert(0, Date)
                l15.config(state='readonly')
            else:
                mssg = "No matching record found."
                l16.config(text=mssg)

    ttk.Label(root, text='Report', font=("Arial", 15, "bold")).grid(row=1, column=0)
    ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=2, column=0, sticky="ew")
    l = ttk.Label(root, text="Enter Your Customer_ID")
    l.grid(row=3, column=0, padx=5, pady=5)
    l = ttk.Entry(root)
    l.grid(row=3, column=1, padx=5, pady=5)

    button = ttk.Button(root, text="Generate Report", command=auto_fill)
    button.grid(row=15, column=0, columnspan=17, padx=5, pady=10)

    l16 = ttk.Label(root, text=" ", font=("Arial", 10, "bold"))
    l16.grid(row=16, columnspan=17)

    root.mainloop()
