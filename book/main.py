from tkinter import *
from tkinter import ttk
from tkinter import messagebox

master =Tk()
master.title('Book Store Program')

def checkBtn():
    if engSub.get():
        yearLevelOne.config(state=NORMAL)
        oneQtyEntry.config(state=NORMAL)
    else:
        oneUPEntry.config(state=NORMAL)
        oneUPEntry.delete(0, END)
        yearLevelOne.set("")
        oneQtyEntry.delete(0, END)
        oneUPEntry.config(state=DISABLED)
        yearLevelOne.config(state=DISABLED)
        oneQtyEntry.config(state=DISABLED)

    if mathSub.get():
        yearLevelTwo.config(state=NORMAL)
        twoQtyEntry.config(state=NORMAL)
    else:
        twoUPEntry.config(state=NORMAL)
        twoUPEntry.delete(0, END)
        yearLevelTwo.set("")
        twoQtyEntry.delete(0, END)
        twoUPEntry.config(state=DISABLED)
        yearLevelTwo.config(state=DISABLED)
        twoQtyEntry.config(state=DISABLED)

    if sciSub.get():
        yearLevelThree.config(state=NORMAL)
        threeQtyEntry.config(state=NORMAL)
    else:
        threeUPEntry.config(state=NORMAL)
        threeUPEntry.delete(0, END)
        yearLevelThree.set("")
        threeQtyEntry.delete(0, END)
        threeUPEntry.config(state=DISABLED)
        yearLevelThree.config(state=DISABLED)
        threeQtyEntry.config(state=DISABLED)

def checkPrice(*args):
    if yearLevelOne.current() == 0:
        oneUPEntry.config(state=NORMAL)
        oneUP.set(150.00)
        oneUPEntry.config(state=DISABLED)
    elif yearLevelOne.current() == 1:
        oneUPEntry.config(state=NORMAL)
        oneUP.set(200.00)
        oneUPEntry.config(state=DISABLED)
    elif yearLevelOne.current() == 2:
        oneUPEntry.config(state=NORMAL)
        oneUP.set(250.00)
        oneUPEntry.config(state=DISABLED)

    if yearLevelTwo.current() == 0:
        twoUPEntry.config(state=NORMAL)
        twoUP.set(150.00)
        twoUPEntry.config(state=DISABLED)
    elif yearLevelTwo.current() == 1:
        twoUPEntry.config(state=NORMAL)
        twoUP.set(200.00)
        twoUPEntry.config(state=DISABLED)
    elif yearLevelTwo.current() == 2:
        twoUPEntry.config(state=NORMAL)
        twoUP.set(250.00)
        twoUPEntry.config(state=DISABLED)

    if yearLevelThree.current() == 0:
        threeUPEntry.config(state=NORMAL)
        threeUP.set(150.00)
        threeUPEntry.config(state=DISABLED)
    elif yearLevelThree.current() == 1:
        threeUPEntry.config(state=NORMAL)
        threeUP.set(200.00)
        threeUPEntry.config(state=DISABLED)
    elif yearLevelThree.current() == 2:
        threeUPEntry.config(state=NORMAL)
        threeUP.set(250.00)
        threeUPEntry.config(state=DISABLED)

def is_pos_integer(value):
    try:
        number = int(value)
        if number > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def compute():
    subTotalOne = 0
    subTotalTwo = 0
    subTotalThree = 0
    if engSub.get():
        if yearLevelOne.current() == -1:
            messagebox.showerror("Level 1 Field Error!", "Must select what Level!")
        elif is_pos_integer(oneQty.get()) == False:
            messagebox.showerror("Quantity 1 Field Error!", "Must input positive integers!")
        elif is_pos_integer(oneQty.get()) == True:
            subTotalOne = oneUP.get() * int(oneQty.get())
            oneSubTotEntry.config(state=NORMAL)
            oneSubTot.set(subTotalOne)
            oneSubTotEntry.config(state=DISABLED)

    if mathSub.get():
        if yearLevelTwo.current() == -1:
            messagebox.showerror("Level 2 Field Error!", "Must select what Level!")
        elif is_pos_integer(twoQty.get()) == False:
            messagebox.showerror("Quantity 2 Field Error!", "Must input positive integers!")
        elif is_pos_integer(twoQty.get()) == True:
            subTotalTwo = twoUP.get() * int(twoQty.get())
            twoSubTotEntry.config(state=NORMAL)
            twoSubTot.set(subTotalTwo)
            twoSubTotEntry.config(state=DISABLED)

    if sciSub.get():
        if yearLevelThree.current() == -1:
            messagebox.showerror("Level 3 Field Error!", "Must select what Level!")
        elif is_pos_integer(threeQty.get()) == False:
            messagebox.showerror("Quantity 3 Field Error!", "Must input positive integers!")
        elif is_pos_integer(threeQty.get()) == True:
            subTotalThree = threeUP.get() * int(threeQty.get())
            threeSubTotEntry.config(state=NORMAL)
            threeSubTot.set(subTotalThree)
            threeSubTotEntry.config(state=DISABLED)

    totalAmount = subTotalOne + subTotalTwo + subTotalThree
    totAmntEntry.config(state=NORMAL)
    totAmnt.set(totalAmount)
    totAmntEntry.config(state=DISABLED)

def clearBTN():
    engCB.deselect()
    mathCB.deselect()
    sciCB.deselect()
    yearLevelOne.set("")
    yearLevelOne.config(state=DISABLED)
    yearLevelTwo.set("")
    yearLevelTwo.config(state=DISABLED)
    yearLevelThree.set("")
    yearLevelThree.config(state=DISABLED)
    oneUPEntry.config(state=NORMAL)
    oneUPEntry.delete(0, END)
    oneUPEntry.config(state=DISABLED)
    twoUPEntry.config(state=NORMAL)
    twoUPEntry.delete(0, END)
    twoUPEntry.config(state=DISABLED)
    threeUPEntry.config(state=NORMAL)
    threeUPEntry.delete(0, END)
    threeUPEntry.config(state=DISABLED)
    oneQtyEntry.delete(0, END)
    oneQtyEntry.config(state=DISABLED)
    twoQtyEntry.delete(0, END)
    twoQtyEntry.config(state=DISABLED)
    threeQtyEntry.delete(0, END)
    threeQtyEntry.config(state=DISABLED)
    oneSubTotEntry.config(state=NORMAL)
    oneSubTotEntry.delete(0, END)
    oneSubTotEntry.config(state=DISABLED)
    twoSubTotEntry.config(state=NORMAL)
    twoSubTotEntry.delete(0, END)
    twoSubTotEntry.config(state=DISABLED)
    threeSubTotEntry.config(state=NORMAL)
    threeSubTotEntry.delete(0, END)
    threeSubTotEntry.config(state=DISABLED)
    totAmntEntry.config(state=NORMAL)
    totAmntEntry.delete(0, END)
    totAmntEntry.config(state=DISABLED)

engSub = BooleanVar()
mathSub = BooleanVar()
sciSub = BooleanVar()
oneUP = IntVar()
twoUP = IntVar()
threeUP = IntVar()
oneQty = StringVar()
twoQty = StringVar()
threeQty = StringVar()
oneSubTot = IntVar()
twoSubTot = IntVar()
threeSubTot = IntVar()
totAmnt = IntVar()

Label(master, text="MJN Book Store", font=("Tahoma", 14)).grid(row=0, sticky=W, padx=5, column=2, pady=10)
Label(master, text="Book Title", font=("Tahoma", 14)).grid(row=1, sticky=W, padx=5)
Label(master, text="Level", font=("Tahoma", 14)).grid(row=1, column=1)
Label(master, text="Unit Price", font=("Tahoma", 14)).grid(row=1, column=2)
Label(master, text="Quantity", font=("Tahoma", 14)).grid(row=1, column=3)
Label(master, text="Sub-Total", font=("Tahoma", 14)).grid(row=1, column=4)
Label(master, text="Total Amount:", font=("Tahoma", 14)).grid(row=5, column=3)

engCB = Checkbutton(master, text="Everyday English", font=("Tahoma", 14), variable=engSub, command=checkBtn)
engCB.grid(row=2, sticky=W, padx=5)
mathCB = Checkbutton(master, text="Integrated Mathematics", font=("Tahoma", 14), variable=mathSub, command=checkBtn)
mathCB.grid(row=3, sticky=W, padx=5)
sciCB = Checkbutton(master, text="Wonders of Science", font=("Tahoma", 14), variable=sciSub, command=checkBtn)
sciCB.grid(row=4, sticky=W, padx=5)

yearLevel = ['NURSERY', 'KINDER', 'PREP']
yearLevelOne = ttk.Combobox(master, values=yearLevel, state="readonly")
yearLevelOne.grid(row=2, column=1)
yearLevelOne.bind("<<ComboboxSelected>>", checkPrice)
yearLevelTwo = ttk.Combobox(master, values=yearLevel, state="readonly")
yearLevelTwo.grid(row=3, column=1)
yearLevelTwo.bind("<<ComboboxSelected>>", checkPrice)
yearLevelThree = ttk.Combobox(master, values=yearLevel, state="readonly")
yearLevelThree.grid(row=4, column=1)
yearLevelThree.bind("<<ComboboxSelected>>", checkPrice)

oneUPEntry = Entry(master, textvariable=oneUP)
oneUPEntry.grid(row=2, column=2)
twoUPEntry = Entry(master, textvariable=twoUP)
twoUPEntry.grid(row=3, column=2)
threeUPEntry = Entry(master, textvariable=threeUP)
threeUPEntry.grid(row=4, column=2)

oneQtyEntry = Entry(master, textvariable=oneQty)
oneQtyEntry.grid(row=2, column=3)
twoQtyEntry = Entry(master, textvariable=twoQty)
twoQtyEntry.grid(row=3, column=3)
threeQtyEntry = Entry(master, textvariable=threeQty)
threeQtyEntry.grid(row=4, column=3)

oneSubTotEntry = Entry(master, textvariable=oneSubTot)
oneSubTotEntry.grid(row=2, column=4, padx=10)
twoSubTotEntry = Entry(master, textvariable=twoSubTot)
twoSubTotEntry.grid(row=3, column=4, padx=10)
threeSubTotEntry = Entry(master, textvariable=threeSubTot)
threeSubTotEntry.grid(row=4, column=4, padx=10)

totAmntEntry = Entry(master, textvariable=totAmnt)
totAmntEntry.grid(row=5, column=4, padx=10, pady=10)

Button(master, text="Compute", font=("Tahoma", 14), width=12, command=compute).grid(row=5, column=1, pady=10)
Button(master, text="Clear", font=("Tahoma", 14), width=12, command=clearBTN).grid(row=5, column=2, pady=10)

clearBTN()

master.mainloop()