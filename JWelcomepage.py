import tkinter as tk
from tkinter import ttk
from BParking_Delete import*
from BParking_Insert import*
from BParking_Show_Search import*
from BParking_Update import*
from CVehicle_Show_Search import *
from CVehicle_Update import *
from CZ_Update_Booking import *
from CZ_Show_Booking import *
from DTransaction_Show_Search import*
from DTransaction_Update import*
from ECustomer_Delete import*
from ECustomer_Insert import*
from ECustomer_Show_Search import*
from FDashboardFloorStatus import *
from FDashboardStatus import *
from GUpdateCust import *
from HReport import*



def FDashboardStatus():
    global rooty
    rooty.withdraw()
    Dashboardstatus()
def FDashboardFloorStatus():
    global rooty
    rooty.withdraw()
    DashBoardFloorStatus()
rooty=""
def Dashboard():
    global rooty
    rooty = tk.Toplevel()
    frame2 = tk.Frame(rooty)               ##frame is created here in which side is shown left with left both username and its box comes in one line
    frame2.pack(pady=10)
    button = ttk.Button(frame2, text="Overall Status", command=FDashboardStatus)
    button.pack(side="left", pady= 40, ipadx=50, ipady=10)
    button = ttk.Button(frame2, text="Floor Status",  command=FDashboardFloorStatus)
    button.pack(side="left", pady=30, ipadx=50, ipady=10)
    rooty.mainloop()

def INsertCunstomer():
    global rootz
    rootz.withdraw()
    Customer_insert()
def DeleteCustomer():
    global rootz
    rootz.withdraw()
    CustomerDElete()
def SHowCustomer():
    global rootz
    rootz.withdraw()
    CustomerShow()
def UpdateCustomer():
    global rootz
    rootz.withdraw()
    CustUpdated()
rootz=""
def Customer():
    global rootz
    rootz = tk.Toplevel()
    frame3 = tk.Frame(rootz)               ##frame is created here in which side is shown left with left both username and its box comes in one line
    frame3.pack(pady=10)
    button = ttk.Button(frame3, text="Insert Customer", command=INsertCunstomer)
    button.pack(side="left", pady= 40, ipadx=50, ipady=10)
    button = ttk.Button(frame3, text="Delete Customer",  command=DeleteCustomer)
    button.pack(side="left", pady=30, ipadx=50, ipady=10)
    button = ttk.Button(frame3, text="Show Customer", command=SHowCustomer)
    button.pack(side="left", pady= 40, ipadx=50, ipady=10)
    button = ttk.Button(frame3, text="Update Customer",  command=UpdateCustomer)
    button.pack(side="left", pady=30, ipadx=50, ipady=10)
    rootz.mainloop()

def INsertParking():
    global rootw
    rootw.withdraw()
    Parkinginsert()
def DeleteParking():
    global rootw
    rootw.withdraw()
    Parkingdelete()
def SHowaparking():
    global rootw
    rootw.withdraw()
    Parkingshow()
def UpdateParking():
    global rootw
    rootw.withdraw()
    ParkingUpdate()
rootw=""
def Parking():
    global rootw
    rootw = tk.Toplevel()
    frame3 = tk.Frame(rootw)               ##frame is created here in which side is shown left with left both username and its box comes in one line
    frame3.pack(pady=10)
    button = ttk.Button(frame3, text="Insert Parking", command=INsertParking)
    button.pack(side="left", pady= 40, ipadx=50, ipady=10)
    button = ttk.Button(frame3, text="Delete Parking",  command=DeleteParking)
    button.pack(side="left", pady=30, ipadx=50, ipady=10)
    button = ttk.Button(frame3, text="Show Parking", command=SHowaparking)
    button.pack(side="left", pady= 40, ipadx=50, ipady=10)
    button = ttk.Button(frame3, text="Update Parking",  command=UpdateParking)
    button.pack(side="left", pady=30, ipadx=50, ipady=10)
    rootw.mainloop()

def Vehiclsearchsss():
    global rootx
    rootx.withdraw()   
    VEhicleShow()
def VehicleUpdatesss():
    global rootx
    rootx.withdraw()
    VehicleUpdate()
rootx=""
def Vehicle():
    global rootx
    rootx = tk.Toplevel()
    frame4 = tk.Frame(rootx)               ##frame is created here in which side is shown left with left both username and its box comes in one line
    frame4.pack(pady=10)
    button = ttk.Button(frame4, text="Vehicle Update", command=VehicleUpdatesss)
    button.pack(side="left", pady= 40, ipadx=50, ipady=10)
    button = ttk.Button(frame4, text="Show Vehicle",  command=Vehiclsearchsss)
    button.pack(side="left", pady=30, ipadx=50, ipady=10)
    # root.withdraw()
    rootx.mainloop()


def BookingShowss():
    global rootf
    rootf.withdraw() 
    BookingShow()
def BookingUpdate():
    global rootf
    rootf.withdraw() 
    Booking_Update()
rootf=""
def Booking():
    global rootf
    rootf = tk.Toplevel()
    frame5 = tk.Frame(rootf)               ##frame is created here in which side is shown left with left both username and its box comes in one line
    frame5.pack(pady=10)
    button = ttk.Button(frame5, text="Show Booking ", command=BookingShowss)
    button.pack(side="left", pady= 40, ipadx=50, ipady=10)
    button = ttk.Button(frame5, text="Booking Update",  command=BookingUpdate)
    button.pack(side="left", pady=30, ipadx=50, ipady=10)
    rootf.mainloop()

def Transactionshow():
    global roott
    roott.withdraw() 
    TrnsactionShow()
def transactionupdate():
    global roott
    roott.withdraw() 
    TrandactionUpdate()
roott=""
def Transaction():
    global roott
    roott = tk.Toplevel()
    frame6 = tk.Frame(roott)               ##frame is created here in which side is shown left with left both username and its box comes in one line
    frame6.pack(pady=10)
    button = ttk.Button(frame6, text="Transaction Show", command=Transactionshow)
    button.pack(side="left", pady= 40, ipadx=50, ipady=10)
    button = ttk.Button(frame6, text="Transaction UPdate",  command=transactionupdate)
    button.pack(side="left", pady=30, ipadx=50, ipady=10)
    roott.mainloop()


def Report():
    report()


    


def Welcome():
    root = tk.Toplevel()
    def Exit():
        root.destroy()
    root.title('Parking System')
    # Make the window full screen
    root.attributes("-fullscreen", True)


    welcome_label = ttk.Label(root, text="Welcome to Parking System", font=('Helvetica', 24))
    welcome_label.pack(pady=20)

    separator = ttk.Separator(root, orient="horizontal")
    separator.pack(fill="x")
    frame1 = tk.Frame(root)               ##frame is created here in which side is shown left with left both username and its box comes in one line
    frame1.pack(pady=10)
    button = ttk.Button(frame1, text="Dashboard", command=Dashboard)
    button.pack(anchor='w', pady= 30, ipadx=50, ipady=7)
    button = ttk.Button(frame1, text="Parking", command=Parking)
    button.pack(anchor='w', pady=25, ipadx=50, ipady=7)   
    button = ttk.Button(frame1, text="Customer", command=Customer)
    button.pack(anchor='w', pady=25, ipadx=50, ipady=7)
    button = ttk.Button(frame1, text="Vehicle", command=Vehicle)
    button.pack(anchor='w', pady=25, ipadx=50, ipady=7)
    button = ttk.Button(frame1, text="Booking", command=Booking)
    button.pack(anchor='w', pady=25, ipadx=50, ipady=7)
    button = ttk.Button(frame1, text="Transaction", command=Transaction)
    button.pack(anchor='w', pady=25, ipadx=50, ipady=7)
    button = ttk.Button(frame1, text="Report", command=Report)
    button.pack(anchor='w', pady=25, ipadx=50, ipady=7)
    button = ttk.Button(frame1, text="Exit", command=Exit)
    button.pack(anchor='w', pady=25, ipadx=50, ipady=7)

    root.mainloop()
