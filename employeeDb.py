import pymysql
from tkinter import *
from tkinter import messagebox


db = pymysql.connect("localhost","root","","EMP")

def insertData():
	cursor = db.cursor()
	sql = "insert into employee values('"+var1.get()+"','"+var2.get()+"',"+var3.get()+");"
	#try:
	cursor.execute(sql)
	db.commit()
	messagebox.showinfo("success","Data inserted!")
	#except:
	print("Error")

def updateData():
	t = Toplevel()
	v1 = StringVar()
	labt = Label(t,text="SSN")
	entt = Entry(t,textvariable=v1)

	v2 = DoubleVar()
	labs = Label(t,text="salary")
	ents = Entry(t,textvariable=v2)

	def s():
		cursor = db.cursor()
		sql = "update employee set salary="+str(v2.get())+"where ssn='"+v1.get()+"';"
		try:
			cursor.execute(sql)
			db.commit()
			messagebox.showinfo("success","Updated")
		except:
			print("Error")


	buts = Button(t,text="update",command=s)

	labt.grid(row=0,column=0)
	entt.grid(row=0,column=1)
	labs.grid(row=1,column=0)
	ents.grid(row=1,column=1)
	buts.grid(row=2,column=0)
	t.mainloop()


def deleteData():
	dt = Toplevel()
	labd = Label(dt,text="ssn")
	vard = StringVar()
	entd = Entry(dt,textvariable=vard)

	def d():
		cursor = db.cursor()
		sql = "delete from employee where ssn='"+vard.get()+"';"
		try:
			cursor.execute(sql)
			db.commit()
			messagebox.showinfo("success","deleted")
		except:
			print("Delete error")
	btd = Button(dt,text="delete",command=d)

	labd.grid(row=0,column=0)
	entd.grid(row=0,column=1)
	btd.grid(row=1,column=0)
	dt.mainloop()


def showData():
	ts = Toplevel()
	labs = Label(ts,text="ssn")
	v1 = StringVar()
	ents = Entry(ts,textvariable=v1)

	def s():
		cursor = db.cursor()
		sql = "select * from employee where ssn='"+v1.get()+"';"

		try:
			cursor.execute(sql)
			results = cursor.fetchall()
			for i in results:
				n = i[0]
				ss = i[1]
				sal = i[2]
			messagebox.showinfo("success",n+"\n"+ss+"\n"+str(sal))

		except:
			print("search error")


	bts = Button(ts,text="search",command=s) 

	labs.grid(row=0,column=0)
	ents.grid(row=0,column=1)
	bts.grid(row=1,column=0)
	ts.mainloop()


w = Tk()
w.title('Employee details')
lab1 = Label(w,text="Name")
var1 = StringVar()
ent1 = Entry(w,textvariable=var1)

lab2 = Label(w,text="ssn")
var2 = StringVar()
ent2 = Entry(w,textvariable=var2)

lab3 = Label(w,text="salary")
var3 = StringVar()
ent3 = Entry(w,textvariable=var3)

b1 = Button(w,text="insert",command=insertData)
b2 = Button(w,text="update",command=updateData)
b3 = Button(w,text="delete",command=deleteData)
b4 = Button(w,text="search",command=showData)



lab1.grid(row=0,column=0)
ent1.grid(row=0,column=1)

lab2.grid(row=1,column=0)
ent2.grid(row=1,column=1)

lab3.grid(row=2,column=0)
ent3.grid(row=2,column=1)

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)
b4.grid(row=4,column=2)


w.mainloop()
