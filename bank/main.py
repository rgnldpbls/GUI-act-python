from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox


master = Tk()
master.title("Simple Bank Program")

def check_button():
    if oneThousand.get():
        oneThouEntry.config(state=NORMAL)
    else:
        oneThouEntry.delete(0, END)
        oneThouEntry.config(state=DISABLED)

    if fiveHundred.get():
        fiveHundEntry.config(state=NORMAL)
    else:
        fiveHundEntry.delete(0, END)
        fiveHundEntry.config(state=DISABLED)

    if twoHundred.get():
        twoHundEntry.config(state=NORMAL)
    else:
        twoHundEntry.delete(0, END)
        twoHundEntry.config(state=DISABLED)

    if oneHundred.get():
        oneHundEntry.config(state=NORMAL)
    else:
        oneHundEntry.delete(0, END)
        oneHundEntry.config(state=DISABLED)

def is_pos_integer(value):
    try:
        number = int(value)
        if number > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def default():
    prevEntry.delete(0, END)
    prevEntry.config(state=DISABLED)
    oneThouCB.deselect()
    fiveHundCB.deselect()
    twoHundCB.deselect()
    oneHundCB.deselect()
    oneThouCB.config(state=DISABLED)
    fiveHundCB.config(state=DISABLED)
    twoHundCB.config(state=DISABLED)
    oneHundCB.config(state=DISABLED)
    oneThouEntry.delete(0, END)
    fiveHundEntry.delete(0, END)
    twoHundEntry.delete(0, END)
    oneHundEntry.delete(0, END)
    oneThouEntry.config(state=DISABLED)
    fiveHundEntry.config(state=DISABLED)
    twoHundEntry.config(state=DISABLED)
    oneHundEntry.config(state=DISABLED)
    oneThouEntry2.config(state=NORMAL)
    oneThouEntry2.delete(0, END)
    oneThouEntry2.config(state=DISABLED)
    fiveHundEntry2.config(state=NORMAL)
    fiveHundEntry2.delete(0, END)
    fiveHundEntry2.config(state=DISABLED)
    twoHundEntry2.config(state=NORMAL)
    twoHundEntry2.delete(0, END)
    twoHundEntry2.config(state=DISABLED)
    oneHundEntry2.config(state=NORMAL)
    oneHundEntry2.delete(0, END)
    oneHundEntry2.config(state=DISABLED)
    prevEntry.delete(0, END)
    totalDepEntry.config(state=NORMAL)
    totalDepEntry.delete(0, END)
    totalDepEntry.config(state=DISABLED)
    curBalEntry.config(state=NORMAL)
    curBalEntry.delete(0, END)
    curBalEntry.config(state=DISABLED)
    compBTN.config(state=DISABLED)

def deposit():
    prevEntry.config(state=NORMAL)
    oneThouCB.config(state=NORMAL)
    fiveHundCB.config(state=NORMAL)
    twoHundCB.config(state=NORMAL)
    oneHundCB.config(state=NORMAL)
    compBTN.config(state=NORMAL)
    prevEntry.delete(0, END)
    curBalEntry.delete(0, END)

def withdraw():
    prevEntry.config(state=NORMAL)
    oneThouCB.config(state=DISABLED)
    fiveHundCB.config(state=DISABLED)
    twoHundCB.config(state=DISABLED)
    oneHundCB.config(state=DISABLED)
    oneThouCB.deselect()
    fiveHundCB.deselect()
    twoHundCB.deselect()
    oneHundCB.deselect()
    oneThouEntry.delete(0, END)
    fiveHundEntry.delete(0, END)
    twoHundEntry.delete(0, END)
    oneHundEntry.delete(0, END)
    oneThouEntry.config(state=DISABLED)
    fiveHundEntry.config(state=DISABLED)
    twoHundEntry.config(state=DISABLED)
    oneHundEntry.config(state=DISABLED)
    oneThouEntry2.config(state=NORMAL)
    oneThouEntry2.delete(0, END)
    oneThouEntry2.config(state=DISABLED)
    fiveHundEntry2.config(state=NORMAL)
    fiveHundEntry2.delete(0, END)
    fiveHundEntry2.config(state=DISABLED)
    twoHundEntry2.config(state=NORMAL)
    twoHundEntry2.delete(0, END)
    twoHundEntry2.config(state=DISABLED)
    oneHundEntry2.config(state=NORMAL)
    oneHundEntry2.delete(0, END)
    oneHundEntry2.config(state=DISABLED)
    prevEntry.delete(0, END)
    totalDepEntry.config(state=NORMAL)
    totalDepEntry.delete(0, END)
    totalDepEntry.config(state=DISABLED)
    curBalEntry.config(state=NORMAL)
    curBalEntry.delete(0, END)
    curBalEntry.config(state=DISABLED)
    compBTN.config(state=NORMAL)
    global withd
    withd = simpledialog.askinteger("Withdraw", "Enter Amount:")

def compute():
    preBal = 0
    oneNop = 0
    twoNop = 0
    threeNop = 0
    fourNop = 0
    firstAmount = 0
    secondAmount = 0
    thirdAmount = 0
    fourthAmount = 0
    totalAmount = 0

    if is_pos_integer(prevBal.get()) == True:
        preBal = int(prevBal.get())
    else:
        messagebox.showerror("Previous Balance Field Error!", "Must input positive integers!")

    if oneThousand.get():
        if is_pos_integer(oneThouPcs.get()) == True:
            oneNop = int(oneThouPcs.get())
        else:
            messagebox.showerror("First Field of Number of Pieces Error!", "Must input positive integers!")

    if fiveHundred.get():
        if is_pos_integer(fiveHundPcs.get()) == True:
            twoNop = int(fiveHundPcs.get())
        else:
            messagebox.showerror("Second Field of Number of Pieces Error!", "Must input positive integers!")

    if twoHundred.get():
        if is_pos_integer(twoHundPcs.get()) == True:
            threeNop = int(twoHundPcs.get())
        else:
            messagebox.showerror("Third Field of Number of Pieces Error!", "Must input positive integers!")

    if oneHundred.get():
        if is_pos_integer(oneHundPcs.get()) == True:
            fourNop = int(oneHundPcs.get())
        else:
            messagebox.showerror("Fourth Field of Number of Pieces Error!", "Must input positive integers!")

    if oneThousand.get():
        firstAmount = 1000 * oneNop
        oneThouEntry2.config(state=NORMAL)
        oneThouAmnt.set(firstAmount)
        oneThouEntry2.config(state=DISABLED)

    if fiveHundred.get():
        secondAmount = 500 * twoNop
        fiveHundEntry2.config(state=NORMAL)
        fiveHundAmnt.set(secondAmount)
        fiveHundEntry2.config(state=DISABLED)

    if twoHundred.get():
        thirdAmount = 200 * threeNop
        twoHundEntry2.config(state=NORMAL)
        twoHundAmnt.set(thirdAmount)
        twoHundEntry2.config(state=DISABLED)

    if oneHundred.get():
        fourthAmount = 100 * fourNop
        oneHundEntry2.config(state=NORMAL)
        oneHundAmnt.set(fourthAmount)
        oneHundEntry2.config(state=DISABLED)


    if firstAmount > 1 or secondAmount > 1 or thirdAmount > 1 or fourthAmount > 1:
        totalAmount = firstAmount + secondAmount + thirdAmount + fourthAmount
        totalDepEntry.config(state=NORMAL)
        totalDep.set(totalAmount)
        totalDepEntry.config(state=DISABLED)

    if totalAmount > 1:
        currentBal = preBal + totalAmount
        curBalEntry.config(state=NORMAL)
        curBal.set(currentBal)
        curBalEntry.config(state=DISABLED)

    elif withd > 1:
        if withd > preBal:
            messagebox.showerror("Warning", "Insufficient Funds!, Your withdraw amount is " + str(withd) + ".")
        else:
            currentBal2 = preBal - withd
            curBalEntry.config(state=NORMAL)
            curBal.set(currentBal2)
            curBalEntry.config(state=DISABLED)


transacType = IntVar()
prevBal = StringVar()
oneThousand = BooleanVar()
fiveHundred = BooleanVar()
twoHundred = BooleanVar()
oneHundred = BooleanVar()
oneThouPcs = StringVar()
fiveHundPcs = StringVar()
twoHundPcs = StringVar()
oneHundPcs = StringVar()
oneThouAmnt = DoubleVar()
fiveHundAmnt = DoubleVar()
twoHundAmnt = DoubleVar()
oneHundAmnt = DoubleVar()
totalDep = DoubleVar()
curBal = DoubleVar()



Label(master, text="Type transaction:", font=("Tahoma", 14)).grid(row=0, sticky=W, padx=5)
Label(master, text="Previous Balance:", font=("Tahoma", 14)).grid(row=1, sticky=W, padx=5)
Label(master, text="Denomination", font=("Tahoma", 14)).grid(row=2, sticky=W, padx=5)
Label(master, text="Number of Pieces", font=("Tahoma", 14)).grid(row=2, column=1)
Label(master, text="Amount", font=("Tahoma", 14)).grid(row=2,column=2)
Label(master, text="Total Deposit:", font=("Tahoma", 14)).grid(row=7,column=1)
Label(master, text="Current Balance:", font=("Tahoma", 14)).grid(row=8, sticky=W, padx=5)

prevEntry = Entry(master, textvariable=prevBal)
prevEntry.grid(row=1, column=1)
oneThouEntry = Entry(master, textvariable=oneThouPcs)
oneThouEntry.grid(row=3, column=1)
fiveHundEntry = Entry(master, textvariable=fiveHundPcs)
fiveHundEntry.grid(row=4, column=1)
twoHundEntry = Entry(master, textvariable=twoHundPcs)
twoHundEntry.grid(row=5, column=1)
oneHundEntry = Entry(master, textvariable=oneHundPcs)
oneHundEntry.grid(row=6, column=1)
oneThouEntry2 = Entry(master, textvariable=oneThouAmnt)
oneThouEntry2.grid(row=3, column=2)
oneThouEntry2.delete(0, END)
fiveHundEntry2 = Entry(master, textvariable=fiveHundAmnt)
fiveHundEntry2.grid(row=4, column=2)
fiveHundEntry2.delete(0, END)
twoHundEntry2 = Entry(master, textvariable=twoHundAmnt)
twoHundEntry2.grid(row=5, column=2)
twoHundEntry2.delete(0, END)
oneHundEntry2 = Entry(master, textvariable=oneHundAmnt)
oneHundEntry2.grid(row=6, column=2)
oneHundEntry2.delete(0, END)
totalDepEntry = Entry(master, textvariable=totalDep)
totalDepEntry.grid(row=7, column=2)
totalDepEntry.delete(0, END)
curBalEntry = Entry(master, textvariable=curBal)
curBalEntry.grid(row=8, column=1)
curBalEntry.delete(0, END)

oneThouCB = Checkbutton(master, text="1,000", font=("Tahoma", 14), variable=oneThousand, command=check_button)
oneThouCB.grid(row=3, sticky=W, padx=5)
fiveHundCB = Checkbutton(master, text="  500", font=("Tahoma", 14), variable=fiveHundred, command=check_button)
fiveHundCB.grid(row=4, sticky=W, padx=5)
twoHundCB = Checkbutton(master, text="  200", font=("Tahoma", 14), variable=twoHundred, command=check_button)
twoHundCB.grid(row=5, sticky=W, padx=5)
oneHundCB = Checkbutton(master, text="  100", font=("Tahoma", 14), variable=oneHundred, command=check_button)
oneHundCB.grid(row=6, sticky=W, padx=5)

transacType.set(1)
Radiobutton(master, text="Default", font=("Tahoma", 14), variable=transacType, value=1, command=default).grid(row=0, column=1)
Radiobutton(master, text="Deposit", font=("Tahoma", 14), variable=transacType, value=2, command=deposit).grid(row=0, column=2)
Radiobutton(master, text="Withdraw", font=("Tahoma", 14), variable=transacType, value=3, command=withdraw).grid(row=0, column=3)

compBTN = Button(master, text="Compute", font=("Tahoma", 14), width=12, command=compute)
compBTN.grid(row=9, column=1, pady=10)

prevEntry.config(state=DISABLED)
oneThouCB.config(state=DISABLED)
oneThouEntry.config(state=DISABLED)
oneThouEntry2.config(state=DISABLED)
fiveHundCB.config(state=DISABLED)
fiveHundEntry.config(state=DISABLED)
fiveHundEntry2.config(state=DISABLED)
twoHundCB.config(state=DISABLED)
twoHundEntry.config(state=DISABLED)
twoHundEntry2.config(state=DISABLED)
oneHundCB.config(state=DISABLED)
oneHundEntry.config(state=DISABLED)
oneHundEntry2.config(state=DISABLED)
totalDepEntry.config(state=DISABLED)
curBalEntry.config(state=DISABLED)
compBTN.config(state=DISABLED)

master.mainloop()