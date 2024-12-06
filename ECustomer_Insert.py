import A0MyModules as m
import re  ## for time 
import tkinter as tk
from tkinter import *
from tkinter import ttk


################### parking table ma bhi jani chahiya kya details abb jo parking id yaha bhra vo kasa bhraga and yaha pa bhari hui id vaha bhi toh honni chahiye. asa kra customer ka alag entry form bhrva la usse
def Customer_insert():
    root = tk.Toplevel()
    root.title('Customer status')

    # Configure ttk style for the separator
    style = ttk.Style()
    style.configure("Horizontal.TSeparator", background="black", thickness=3)

    def Insert(*args): 
        selected_status = Floor.get()
        print(selected_status)
        if selected_status:
            query3 = f"select count(Available) from booking where floor  = '{selected_status}';"
            query2 = f"SELECT (select Total from parking where Floor = '{selected_status}') - (select count(Available) from booking where floor  = '{selected_status}');"
        else:
            mssg = "Invalid plot status"
            l5.config(text=mssg)

        result2 = m.SqlConnectivity_Show_Search_DashboardStatus_TotalParking1(query2)
        result3 = m.SqlConnectivity_Show_Search_DashboardStatus_TotalParking1(query3)
        if result2 and result3: 
            Available, Booked = result2[0], result3[0]
            l31.config(text=Available)
            l32.config(text=Booked)

        Cust_ID = l2.get()
        First_Name = l0.get()
        Last_Name = l4.get()
        Phone = l6.get()
        Address = l8.get()
        Vehicle_Num = l10.get()
        VType = l12.get()
        Color = l14.get()
        Company = l16.get()
        Transaction_ID = l18.get()
        TType = l20.get()
        Amount = l22.get()
        In_Time = l24.get()
        Out_Time = l26.get()
        Date = l28.get()
        Booking_Slot_Num = l29.get()
        selected_floor = Floor.get()  # Get the selected floor value
        Avail = l31.cget("text")   ## get the value of text
        Available = Avail[0]  # Extract the value from the tuple ## just to see what Avail is getting us
        # print(Available)
        # if len(Cust_ID) == 0 or len(First_Name)==0 or len(Last_Name)==0 or len(Phone)==0 or len(Address)==0 or len(Vehicle_Num) == 0 or len(VType) == 0 or len(Color) == 0 or len(Company)==0 or len(Transaction_ID) == 0 or len(TType) == 0 or len(Amount) == 0 or len(In_Time)==0 or len(Out_Time)==0 or len(Date)==0 or len(Booking_Slot_Num)==0:
        if len(Cust_ID) == 0:
            mssg = "Enter a valid Customer ID"
            l5.config(text=mssg)
        elif not First_Name.isalpha() or len(First_Name)==0:
            mssg = "Enter a valid First Name "
            l5.config(text=mssg)
        elif not Last_Name.isalpha() or len(First_Name)==0:
            mssg = "Enter a valid Last Name "
            l5.config(text=mssg)
        elif not Phone.isdigit() or len(Phone) != 10:
            mssg = "Enter a valid 10-digit phone number"
            l5.config(text=mssg)
        elif len(Address) == 0:
            mssg = "Enter a valid Address"
            l5.config(text=mssg)
        elif len(Vehicle_Num) == 0:
            mssg = "Enter a valid Vehicle Num"
            l5.config(text=mssg)
        elif not VType.isalpha() or len(VType)==0:
            mssg = "Enter a valid Type of vehicle "
            l5.config(text=mssg)
        elif not Color.isalpha() or len(Color)==0:
            mssg = "Enter a valid Color"
            l5.config(text=mssg)
        elif not Company.isalpha() or len(Company)==0:
            mssg = "Enter a valid Company "
            l5.config(text=mssg)
        elif len(Transaction_ID) == 0:
            mssg = "Enter a valid Transaction ID"
            l5.config(text=mssg)
        elif not TType.isalpha() or len(TType)==0:
            mssg = "Enter a Valid Mode of payment "
            l5.config(text=mssg)
        elif not Amount.isdigit() or len(Amount)==0:
            mssg = "Enter a valid Amount "
            l5.config(text=mssg)
        elif not re.match(r'^\d{2}:\d{2}:\d{2}$', In_Time) or len(In_Time)==0:
            mssg = "Enter a valid IN time in the format HH:mm:ss"
            l5.config(text=mssg)
        elif not re.match(r'^\d{2}:\d{2}:\d{2}$', Out_Time) or len(Out_Time)==0:
            mssg = "Enter a valid OUT time in the format HH:mm:ss"
            l5.config(text=mssg)
        elif not re.match(r'^\d{4}-\d{2}-\d{2}$', Date)or len(Date)==0:
            mssg = "Enter a valid Date in the format YYYY-MM-DD"
            l5.config(text=mssg)
        elif len(Booking_Slot_Num) == 0:
            mssg = "Enter a valid Booking Slot"
            l5.config(text=mssg)

        else:
            query1 = f"insert into customer values ('{Cust_ID}','{Booking_Slot_Num}','{Transaction_ID}','{Vehicle_Num}','{First_Name}','{Last_Name}', '{Phone}', '{Address}');"
            query2 = f"insert into vehicle values ('{Vehicle_Num}', '{VType}', '{Color}' , '{Company}');"
            query3 = f"insert into transaction values ('{Transaction_ID}', '{TType}', '{Amount}' , '{In_Time}', '{Out_Time}', '{Date}');"
            query4 = f"insert into booking (Booking_Slot_Num, Floor, Available) values ('{Booking_Slot_Num}', '{selected_floor}', '{Available}');"

        mssg=""
        e=m.SqlConnectivity_Insert1(query1)
        if e ==1 :
            mssg =mssg+ "Customer added Success\n"
            e=m.SqlConnectivity_Insert1(query2)
            if e ==1 :
                mssg = mssg+"vehicla added Success\n"
                # l5.config(text=mssg)
            elif(e==0):
                mssg+="v not added "

            else:
                mssg = mssg+"Error: Place Vehicle Num already exists\n"  
            e=m.SqlConnectivity_Insert1(query3)
            if e ==1 :
                mssg = mssg+"Transaction added Success\n"
                # l5.config(text=mssg)
            elif(e==0):
                mssg+="T not added "

            else:
                mssg = mssg+"Error: Place transaction ID already exists\n"  
            e=m.SqlConnectivity_Insert1(query4)
            if e ==1 :
                mssg = mssg+"booking added Success\n"
                # l5.config(text=mssg)
            elif(e==0):
                mssg+="b not added "

            else:
                mssg = mssg+"Error: Place Booking ID already exists."  
                # l5.config(text=mssg)

            # l5.config(text=mssg)
        elif(e==0):
            mssg+="Customer not added "

        else:
            # mssg = mssg+"Error: Place Customer ID already exists.\n"
            mssg = mssg+"Vehicle not added because customer not valid \n"
            mssg = mssg+"Booking not added because customer not valid\n"
            mssg = mssg+"Transaction not added because customer not valid\n"
            # l5.config(text=mssg)         
        
        l5.config(text=mssg)



    # ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=0 ,columnspan=2, sticky="ew")
    ttk.Label(root, text='Customers Details', font=("Arial", 15, "bold")).grid(row=1, column=1)
    ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=2, columnspan=2, sticky="ew")

    l1 = ttk.Label(root, text="Customer ID")
    l1.grid(row=3, column=1,  padx=10, pady=10)
    l2 = ttk.Entry(root)
    l2.grid(row=3, column=2,  padx=10, pady=10)


    l = ttk.Label(root, text="First Name")
    l.grid(row=3, column=3,  padx=10, pady=10)
    l0 = ttk.Entry(root)
    l0.grid(row=3, column=4,  padx=10, pady=10)

    l3 = ttk.Label(root, text=" Last Name")
    l3.grid(row=3, column=5,  padx=10, pady=10)
    l4 = ttk.Entry(root)
    l4.grid(row=3, column=6,  padx=10, pady=10)

    l5 = ttk.Label(root, text="Phone")
    l5.grid(row=3, column=7,  padx=10, pady=10)
    l6 = ttk.Entry(root)
    l6.grid(row=3, column=8,  padx=10, pady=10)

    l7 = ttk.Label(root, text="Address")
    l7.grid(row=3, column=9,  padx=10, pady=10)
    l8 = ttk.Entry(root)
    l8.grid(row=3, column=10,  padx=10, pady=10)

    # ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=4, columnspan=2, sticky="ew")
    ttk.Label(root, text='Vehicle Details', font=("Arial", 15, "bold")).grid(row=5, column=1)
    ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=6, columnspan=2, sticky="ew")

    l9 = ttk.Label(root, text="Vehicle Number")
    l9.grid(row=7, column=1,  padx=10, pady=10,)
    l10 = ttk.Entry(root)
    l10.grid(row=7, column=2,  padx=10, pady=10)

    l11 = ttk.Label(root, text="Type of Vehicle")
    l11.grid(row=7, column=3,  padx=10, pady=10)
    l12 = ttk.Entry(root)
    l12.grid(row=7, column=4,  padx=10, pady=10)


    l13 = ttk.Label(root, text="Color of Vehicle")
    l13.grid(row=7, column=5,  padx=10, pady=10)
    l14 = ttk.Entry(root)
    l14.grid(row=7, column=6,  padx=10, pady=10)

    l15 = ttk.Label(root, text="Company of Vehicle")
    l15.grid(row=7, column=7,  padx=10, pady=10)
    l16 = ttk.Entry(root)
    l16.grid(row=7, column=8,  padx=10, pady=10)

    # ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=8, columnspan=2, sticky="ew")
    ttk.Label(root, text='Transaction', font=("Arial", 15, "bold")).grid(row=9, column=1)
    ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=10, columnspan=2, sticky="ew")

    l17 = ttk.Label(root, text="Transaction ID")
    l17.grid(row=11, column=1,  padx=10, pady=10,)
    l18 = ttk.Entry(root)
    l18.grid(row=11, column=2,  padx=10, pady=10)

    l19 = ttk.Label(root, text="Mode of payment")
    l19.grid(row=11, column=3,  padx=10, pady=10)
    l20 = ttk.Entry(root)
    l20.grid(row=11, column=4,  padx=10, pady=10)


    l21 = ttk.Label(root, text="Amount")
    l21.grid(row=11, column=5,  padx=10, pady=10)
    l22 = ttk.Entry(root)
    l22.grid(row=11, column=6,  padx=10, pady=10)

    l23 = ttk.Label(root, text="In Time")
    l23.grid(row=11, column=7,  padx=10, pady=10)
    l24 = ttk.Entry(root)
    l24.grid(row=11, column=8,  padx=10, pady=10)

    l25 = ttk.Label(root, text="Out Time")
    l25.grid(row=11, column=9,  padx=10, pady=10)
    l26 = ttk.Entry(root)
    l26.grid(row=11, column=10,  padx=10, pady=10)

    l27 = ttk.Label(root, text="Date")
    l27.grid(row=11, column=11,  padx=10, pady=10)
    l28 = ttk.Entry(root)
    l28.grid(row=11, column=12,  padx=10, pady=10)
    # ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=12, columnspan=2, sticky="ew")

    ttk.Label(root, text='Booking', font=("Arial", 15, "bold")).grid(row=12, column=1)
    ttk.Separator(root, orient=tk.HORIZONTAL).grid(row=13, columnspan=2, sticky="ew")
    l29 = ttk.Label(root, text="Booking Slot Num")
    l29.grid(row=14, column=1,  padx=10, pady=10,)
    l29 = ttk.Entry(root)
    l29.grid(row=14, column=2,  padx=10, pady=10)



    Floor = StringVar()
    l30 = ttk.Label(root, text="Floor")
    l30.grid(row=14, column=3,  padx=10, pady=10)
    query4 = "select Floor from parking"
    result4 = m.SqlConnectivity_Show_Search_DashboardStatus_TotalParking1(query4)
    # print(result4)   ## will give tupple ## no use here 
    default_value = result4[0][0]  # Choose the desired default value from result4 ## [0][0] to get value from tupple
    # Create a dropdown menu for plot status selection
    status_dropdown = ttk.OptionMenu(root, Floor, default_value, *result4) ## *result4, we are unpacking the elements of result4 and passing them as separate arguments.
    status_dropdown.grid(row=14, column=4, padx=10, pady=10)



    l31 = ttk.Label(root, text="Available")
    l31.grid(row=14, column=5,  padx=10, pady=10)
    l31 = ttk.Label(root, text="")
    l31.grid(row=14, column=6,  padx=10, pady=10)

    l32 = ttk.Label(root, text="Booked")
    l32.grid(row=14, column=7,  padx=10, pady=10)
    l32 = ttk.Label(root, text="")
    l32.grid(row=14, column=8,  padx=10, pady=10)

    button = ttk.Button(root, text="Insert", command=Insert)
    button.grid(row=16, column=3, columnspan = 5, padx=(40, 20), pady=10)

    l5 = ttk.Label(root, text=" ", font=("Arial", 10, "bold"))
    l5.grid(row=17, column=3, columnspan=5)
    Floor.trace("w", Insert)

    # Call the Check function to display initial results
    Insert()

    root.mainloop()


