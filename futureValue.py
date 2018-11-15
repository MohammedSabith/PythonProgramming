'''
Write a program that calculates the future value of an investment at a given interest
rate for a specified number of years. The formula for the calculation is as follows:
futureValue = investmentAmount * (1 + monthlyInterestRate) years* 12
Use text fields for users to enter the investment amount, years, and interest rate.
Display the future amount in a label field when the user clicks the Calculate button,
as shown.
'''

from tkinter import *

w = Tk()
w.title("Future value")
var1 = DoubleVar()
var2 = DoubleVar()
var3 = DoubleVar()

lab1 = Label(w,text="Investment amount")
lab2 = Label(w,text="Years")
lab3 = Label(w,text="Annual Interest Rate")
lab4 = Label(w,text="Future value")
lab5 = Label(w)

ent1 = Entry(w,textvariable=var1)
ent2 = Entry(w,textvariable=var2)
ent3 = Entry(w,textvariable=var3)

def compute():
	inAmt = var1.get()
	mir = var3.get()
	# mir = mir / 12
	y = var2.get()

	futureValue = inAmt * ((1 + mir)**(y * 12))

	lab5.config(text=futureValue)


b1 = Button(w,text="calculate",command=compute)

lab1.grid(row=0,column=0)
lab2.grid(row=1,column=0)
lab3.grid(row=2,column=0)
lab4.grid(row=3,column=0)

ent1.grid(row=0,column=1)
ent2.grid(row=1,column=1)
ent3.grid(row=2,column=1)

lab5.grid(row=3,column=1)
b1.grid(row=4,column=1)

w.mainloop()
