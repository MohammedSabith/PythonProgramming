# ----------- Execute the program using Python version 3 ---------------# 
# ----------- For Python 2.7 - use MySQLdb instead of pymysql -----------# 
''' Steps to be follwoed before the exeution of this program:
1 - Loin to mysql
2 - Create database STUD  
3 - create table student  
		student( usn varchar(10),name varchar(10),age int,branch varchar(10),place varchar(20))'''

import tkinter
import pymysql
from tkinter import messagebox

window = tkinter.Tk()
var1=tkinter.StringVar()
var2=tkinter.StringVar()
var3=tkinter.IntVar()
var4=tkinter.StringVar()
var5=tkinter.StringVar()

def Insert():	
	db = pymysql.connect("localhost","root","","STUD")
	cursor = db.cursor()
	sql = "INSERT INTO student VALUES ('%s','%s',%d,'%s','%s')"%(var1.get(),var2.get(),var3.get(),var4.get(),var5.get())
	try:
		cursor.execute(sql)
		db.commit()
		messagebox.showinfo("Success","Successfully inserted")
	except:
		messagebox.showerror("Error","Something Wrong")
	db.close()

def Search():
	w =tkinter.Toplevel()
	v1=tkinter.StringVar()
	def s():
		if(v1.get()==""):
			messagebox.showinfo("Info","Enter USN")
		else:
			db = pymysql.connect("localhost","root","","STUD" )
			cursor = db.cursor()
			sql = "SELECT * FROM student WHERE usn = '%s'" %(v1.get())
			try:
				cursor.execute(sql)
				results = cursor.fetchall()
				for row in results:
					usn = row[0]
					name = row[1]
					age = row[2]
					branch = row[3]
					place = row[4]
				messagebox.showinfo("Student Details","usn=%s,name=%s,age=%d,branch=%s,place=%s"%(usn,name,age,branch,place))			
			except:
				messagebox.showinfo("Sorry","No records found")
			db.close()
	
	l1 = tkinter.Label(w,text="USN")
	e1 = tkinter.Entry(w,textvariable=v1)

	b1= tkinter.Button(w, text ="Search",command=s)
	
	l1.grid(row=0,column=0)
	e1.grid(row=0,column=1)
	b1.grid(row=1,column=0)
	w.mainloop()

label1 = tkinter.Label(window, text="USN")
entry1 = tkinter.Entry(window,textvariable=var1)

label2 = tkinter.Label(window, text="FName")
entry2 = tkinter.Entry(window,textvariable=var2)

label3 = tkinter.Label(window, text="Age")
entry3 = tkinter.Entry(window,textvariable=var3)

label4 = tkinter.Label(window, text="Branch")
entry4 = tkinter.Entry(window,textvariable=var4)

label5 = tkinter.Label(window, text="Place")
entry5 = tkinter.Entry(window,textvariable=var5)

button1= tkinter.Button(window, text ="Insert Student Details",command=Insert)
button2= tkinter.Button(window, text ="Search",command=Search)

label1.grid(row=0,column=0)
entry1.grid(row=0,column=1)

label2.grid(row=1,column=0)
entry2.grid(row=1,column=1)

label3.grid(row=2,column=0)
entry3.grid(row=2,column=1)

label4.grid(row=3,column=0)
entry4.grid(row=3,column=1)

label5.grid(row=4,column=0)
entry5.grid(row=4,column=1)

button1.grid(row=5,column=0)
button2.grid(row=5,column=1)

window.mainloop()
