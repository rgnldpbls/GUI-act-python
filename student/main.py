from tkinter import *
from tkinter import ttk
from tkinter import messagebox


master = Tk()
master.title("Student Slip")

def is_pos_integer(value):
    try:
        number = int(value)
        if number > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def clearBTN():
    studEntry.delete(0, END)
    unitEntry.delete(0, END)
    yearLevelCB.set("")
    LabFee.set(0)
    StudCoun.set(0)
    RegCard.set(0)
    StudID.set(0)
    Cat.set(0)
    OtherMisc.set(0)
    scholGrant.set(1)
    totAmEntry.config(state=NORMAL)
    totAmEntry.delete(0, END)
    totAmEntry.config(state=DISABLED)

def computeBTN():
    yearLevelFee = 0
    if studName.get() == "":
        messagebox.showerror("Student Name Field Error!", "Must input Student Name!")
    elif is_pos_integer(unitEnroll.get()) == True:
        if yearLevelCB.current() == -1:
            messagebox.showerror("Year Level Field Error!", "Must select what year level!")
        elif yearLevelCB.current() == 0:
            yearLevelFee += 100
        elif yearLevelCB.current() == 1:
            yearLevelFee += 200
        elif yearLevelCB.current() == 2:
            yearLevelFee += 300
        elif yearLevelCB.current() == 3:
            yearLevelFee += 400
        elif yearLevelCB.current() == 4:
            yearLevelFee += 500

        otherFees = LabFee.get() + StudCoun.get() + RegCard.get() + StudID.get() + Cat.get() + OtherMisc.get()

        if scholGrant.get() == 1:
            totAmnt = (int(unitEnroll.get()) * 10) + yearLevelFee + otherFees
        elif scholGrant.get() == 2:
            totAmnt = 0
        elif scholGrant.get() == 3:
            totAmnt = ((int(unitEnroll.get()) * 10) + yearLevelFee + otherFees) / 2

        totAmEntry.config(state=NORMAL)
        totalAmount.set(totAmnt)
        totAmEntry.config(state=DISABLED)
    else:
        messagebox.showerror("Units Enrolled Field Error!", "Must input positive integers!")


studName = StringVar()
unitEnroll = StringVar()
LabFee = IntVar()
StudCoun = IntVar()
RegCard = IntVar()
StudID = IntVar()
Cat = IntVar()
OtherMisc = IntVar()
scholGrant = IntVar()
totalAmount = DoubleVar()

Label(master, text="Please enter needed details below:", font=("Tahoma", 18, "bold")).grid(row=0, sticky=N, pady=10, padx=5)
Label(master, text="Student Name:", font=("Tahoma", 14)).grid(row=1, sticky=W, padx=5)
Label(master, text="Units Enrolled:", font=("Tahoma", 14)).grid(row=2, sticky=W, padx=5)
Label(master, text="Year Level:", font=("Tahoma", 14)).grid(row=3, sticky=W, padx=5)
Label(master, text="Other Fees:", font=("Tahoma", 14)).grid(row=4, sticky=W, padx=5)
Label(master, text="Scholarship Grants:", font=("Tahoma", 14)).grid(row=8, sticky=W, padx=5)
Label(master, text="Total Amount:", font=("Tahoma", 14)).grid(row=11, sticky=W, padx=5)

studEntry = Entry(master, textvariable=studName)
studEntry.grid(row=1, column=0)
unitEntry = Entry(master, textvariable=unitEnroll)
unitEntry.grid(row=2, column=0)
unitEntry.delete(0, END)
yearLevel = ['1st Year', '2nd Year', '3rd Year', '4th Year', '5th Year']
yearLevelCB = ttk.Combobox(master, values=yearLevel, state="readonly")
yearLevelCB.grid(row=3, column=0)
Checkbutton(master, text="Laboratory Fee      P200", font=("Tahoma", 14), variable=LabFee, onvalue=200, offvalue=0).grid(row=5, sticky=W, padx=5)
Checkbutton(master, text="Student Council      P50  ", font=("Tahoma", 14), variable=StudCoun, onvalue=50, offvalue=0).grid(row=5, column=1)
Checkbutton(master, text="Registration Card   P50", font=("Tahoma", 14), variable=RegCard, onvalue=50, offvalue=0).grid(row=6, sticky=W, padx=5)
Checkbutton(master, text="Student ID             P50  ", font=("Tahoma", 14), variable=StudID, onvalue=50, offvalue=0).grid(row=6, column=1)
Checkbutton(master, text="Catalyst\t\tP50", font=("Tahoma", 14), variable=Cat, onvalue=50, offvalue=0).grid(row=7, sticky=W, padx=5)
Checkbutton(master, text="Other Miscellaneous P100 ", font=("Tahoma", 14), variable=OtherMisc, onvalue=100, offvalue=0).grid(row=7, column=1)
scholGrant.set(1)
Radiobutton(master, text="Non-Scholar\t        ", font=("Tahoma", 14), variable=scholGrant, value=1).grid(row=8, sticky=E, column=0)
Radiobutton(master, text="Full Scholar\t        ", font=("Tahoma", 14), variable=scholGrant, value=2).grid(row=9, sticky=E, column=0)
Radiobutton(master, text="Partial Scholar\t        ", font=("Tahoma", 14), variable=scholGrant, value=3).grid(row=10, sticky=E, column=0)
totAmEntry = Entry(master, textvariable=totalAmount, state=DISABLED)
totAmEntry.grid(row=11, column=0)
totAmEntry.config(state=NORMAL)
totAmEntry.delete(0, END)
totAmEntry.config(state=DISABLED)
Button(master, text="COMPUTE", font=("Tahoma", 14), width=12, command=computeBTN).grid(row=12, sticky=W, pady=10, padx= 150)
Button(master, text="CLEAR", font=("Tahoma", 14), width=12, command=clearBTN).grid(row=12, sticky=W, column=1)

master.mainloop()