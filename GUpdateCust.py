
import A0MyModules as m
import re  ## for time 
import tkinter as tk
from tkinter import *
from tkinter import ttk
def CustUpdated():
    root = tk.Toplevel()

    root.title("Update Records")
    def hide_auto_fill_button():
        # Hide the "Auto Fill" button
        button.grid_remove()
    def auto_fill():
        Cust_ID  = l.get()
        ## making all global so that they can be accesed in further functions
        global  l0, l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15
        if len(Cust_ID) == 0:
            mssg = "You haven't filled all the required details."
            l16.config(text=mssg)
        else:
            l0 = ttk.Label(root, text="Booking Slot Number ")
            l0.grid(row=2, column=0, padx=3, pady=30)
            l0 = ttk.Entry(root)
            l0.grid(row=2, column=1, padx=3, pady=30)


            l1 = ttk.Label(root, text="Transaction ID")
            l1.grid(row=2, column=2, padx=3, pady=30)
            l1 = ttk.Entry(root)
            l1.grid(row=2, column=3, padx=3, pady=30)

            l2 = ttk.Label(root, text="Vehicle Number")
            l2.grid(row=2, column=4, padx=3, pady=30)
            l2 = ttk.Entry(root)
            l2.grid(row=2, column=5, padx=3, pady=30)

            l3 = ttk.Label(root, text="First Name")
            l3.grid(row=2, column=6, padx=3, pady=30)
            l3 = ttk.Entry(root)
            l3.grid(row=2, column=7, padx=3, pady=30)

            l4 = ttk.Label(root, text="Last Name")
            l4.grid(row=2, column=8, padx=3, pady=30)
            l4 = ttk.Entry(root)
            l4.grid(row=2, column=9, padx=3, pady=30)

            l5 = ttk.Label(root, text="Phone")
            l5.grid(row=2, column=10, padx=3, pady=30)
            l5 = ttk.Entry(root)
            l5.grid(row=2, column=11, padx=3, pady=30)

            l6 = ttk.Label(root, text="Address")
            l6.grid(row=2, column=12, padx=3, pady=30)
            l6 = ttk.Entry(root)
            l6.grid(row=2, column=13, padx=3, pady=30)


            l7 = ttk.Label(root, text="Floor ")
            l7.grid(row=3, column=0, padx=10, pady=20)
            l7 = ttk.Entry(root)
            l7.grid(row=3, column=1, padx=10, pady=20)

            l8 = ttk.Label(root, text="Type Of Vehicle")
            l8.grid(row=4, column=0, padx=10, pady=20)
            l8 = ttk.Entry(root)
            l8.grid(row=4, column=1, padx=10, pady=20)

            l9 = ttk.Label(root, text="Color")
            l9.grid(row=4, column=2, padx=10, pady=20)
            l9 = ttk.Entry(root)
            l9.grid(row=4, column=3, padx=10, pady=20)

            l10 = ttk.Label(root, text="Company")
            l10.grid(row=4, column=4, padx=10, pady=20)
            l10 = ttk.Entry(root)
            l10.grid(row=4, column=5, padx=10, pady=20)

            l11 = ttk.Label(root, text="Type Of Transaction")
            l11.grid(row=5, column=0, padx=10, pady=20)
            l11 = ttk.Entry(root)
            l11.grid(row=5, column=1, padx=10, pady=20)

            l12 = ttk.Label(root, text="Amount")
            l12.grid(row=5, column=2, padx=10, pady=20)
            l12 = ttk.Entry(root)
            l12.grid(row=5, column=3, padx=10, pady=20)

            l13 = ttk.Label(root, text="In Time")
            l13.grid(row=5, column=4, padx=10, pady=20)
            l13 = ttk.Entry(root)
            l13.grid(row=5, column=5, padx=10, pady=20)

            l14 = ttk.Label(root, text="Out Time")
            l14.grid(row=5, column=6, padx=10, pady=20)
            l14 = ttk.Entry(root)
            l14.grid(row=5, column=7, padx=10, pady=20)

            l15 = ttk.Label(root, text="Date")
            l15.grid(row=5, column=8, padx=10, pady=20)
            l15 = ttk.Entry(root)
            l15.grid(row=5, column=9, padx=10, pady=20)

            query1 = f"SELECT Booking_Slot_Num,Transaction_ID , Vehicle_Num, First_Name ,Last_Name ,Phone ,Address FROM customer WHERE Cust_ID = '{Cust_ID}';"
            result1 = m.Auto_Fill(query1)
            print(result1[0])  ## shows it is working properly====== Very Very Imp
            print(result1[1]) 
            print(result1[2]) 
            query2 = f"SELECT Floor from booking WHERE Booking_Slot_Num = '{result1[0]}';"
            result2 = m.Auto_Fill(query2)
            print(result2[0])
            query3 = f"SELECT Type,Color,Company from vehicle WHERE Vehicle_Num = '{result1[2]}';"
            result3 = m.Auto_Fill(query3)
            print(result3[0])
            query4 = f"SELECT Type,Amount,In_Time,Out_Time,Date from transaction WHERE Transaction_ID = '{result1[1]}';"
            result4 = m.Auto_Fill(query4)
            # print(result4[0])
            if result1[0] and result1[1] and result1[2] and result1[3] and result1[4] and result1[5] and result1[6]  and result2[0]  and result3[0] and result3[1] and result3[2] and result4[0] and result4[1] and result4[2] and result4[3] and result4[4]  :
                Booking_Slot_Num =  result1[0]   ## 0 will select first value from tupple ## index starts with 0
                Transaction_ID = result1[1]   ## 1 qill select second value from tupple
                Vehicle_Num = result1[2]
                First_Name = result1[3]
                Last_Name = result1[4]
                Phone =  result1[5]
                Address =  result1[6]
                Floor = result2[0]
                Type = result3[0]
                Color = result3[1]
                Company = result3[2]
                Type_Transaction = result4[0]
                Amount= result4[1]
                In_Time= result4[2]
                Out_Time= result4[3]
                Date =result4[4]
                l0.insert(0, Booking_Slot_Num)
                l0.config(state='readonly')
                l1.insert(0, Transaction_ID)
                l1.config(state='readonly')
                l2.insert(0, Vehicle_Num)
                l2.config(state='readonly')
                l3.insert(0, First_Name)
                l4.insert(0, Last_Name)
                l5.insert(0, Phone)
                l6.insert(0, Address)
                l7.insert(0, Floor)
                l8.insert(0, Type)
                l9.insert(0, Color)
                l10.insert(0, Company)
                l11.insert(0, Type_Transaction)
                l12.insert(0, Amount)
                l13.insert(0, In_Time)
                l14.insert(0, Out_Time)
                l15.insert(0, Date)
                hide_auto_fill_button()  # Hide the "Auto Fill" button

            else:
                mssg = "No matching record found."
                l16.config(text=mssg)
            button = ttk.Button(root, text="Update", command=Update_Record)              ## overriding AutoFill BUtton
            button.grid(row=15, column=0, columnspan=17, padx=5, pady=10)

    def Update_Record():
        Cust_ID  = l.get()
        Booking_Slot_Num =  l0.get()   
        Transaction_ID =  l1.get() 
        Vehicle_Num =  l2.get() 
        First_Name = l3.get()
        Last_Name = l4.get()
        First_Name = l3.get() 
        Last_Name = l4.get() 
        Phone =  l5.get() 
        Address =  l6.get() 
        Floor = l7.get() 
        Type = l8.get() 
        Color = l9.get() 
        Company = l10.get() 
        Type_Transaction = l11.get() 
        Amount= l12.get() 
        In_Time= l13.get() 
        Out_Time= l14.get() 
        Date =l15.get() 

        if len(Cust_ID) == 0 or len(First_Name)==0 or len(Booking_Slot_Num)==0 or len(Last_Name)==0 or len(Phone)==0 or len(Address)==0 or len(Vehicle_Num) == 0 or len(Type_Transaction) == 0 or len(Color) == 0 or len(Company)==0 or len(Transaction_ID) == 0 or len(Type) == 0 or len(Amount) == 0 or len(In_Time)==0 or len(Out_Time)==0 or len(Date)==0 or len(Floor)==0:
            mssg = "You haven't filled the required details."
            l16.config(text=mssg)
        else:
            query1 = f"UPDATE customer SET Booking_Slot_Num = '{Booking_Slot_Num}', Transaction_ID='{Transaction_ID}',  Vehicle_Num='{Vehicle_Num}',  First_Name='{First_Name}',  Last_Name='{Last_Name}' , Phone='{Phone}',  Address='{Address}' WHERE Cust_ID = '{Cust_ID}';"
            result1 = m.SqlConnectivity_Update_record1(query1)
            query2 = f"UPDATE vehicle SET Vehicle_Num='{Vehicle_Num}',  Type='{Type}',  Color='{Color}' , Company='{Company}' WHERE Vehicle_Num='{Vehicle_Num}';"       
            result2 = m.SqlConnectivity_Update_record1(query2)
            query3 = f"UPDATE Booking SET Booking_Slot_Num='{Booking_Slot_Num}',  Floor='{Floor}' WHERE Booking_Slot_Num='{Booking_Slot_Num}';"       
            result3 = m.SqlConnectivity_Update_record1(query3)
            query4 = f"UPDATE transaction SET Transaction_ID='{Transaction_ID}',  Type='{Type_Transaction}' , Amount='{Amount}', In_Time='{In_Time}', Out_Time='{Out_Time}', Date='{Date}' WHERE Transaction_ID='{Transaction_ID}';"       
            result4 = m.SqlConnectivity_Update_record1(query4)
            if result1:
                mssg = "Successful"
                l16.config(text=mssg)
            elif result2:
                mssg = "Successful"
                l16.config(text=mssg)
            elif result3:
                mssg = "Successful"
                l16.config(text=mssg)
            elif result4:
                mssg = "Successful"
                l16.config(text=mssg)
            else:
                mssg = "Already Updated"
                l16.config(text=mssg)  

    

    l = ttk.Label(root, text="Enter Your Customer_ID")
    l.grid(row=1, column=0)
    l = ttk.Entry(root)
    l.grid(row=1, column=1)


    button = ttk.Button(root, text="Auto Fill", command=auto_fill)
    button.grid(row=17, column=0, columnspan=17, padx=5, pady=10)

    l16 = ttk.Label(root, text=" ", font=("Arial", 10, "bold"))
    l16.grid(row=16, column=0, columnspan=17)


    root.mainloop()


