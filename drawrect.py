from tkinter import *

w = Tk()
w.title("Draw fill fun")

can = Canvas(w,width=200,height=200)

def draw():
	can.delete(ALL)
	shape = vars.get()
	filled = varf.get()

	if(shape == "rect"):
		if(filled == 1):
			can.create_rectangle(10,10,180,180,fill="cyan")
		else:
			can.create_rectangle(10,10,180,180)

	elif(shape == "oval"):
		if(filled == 1):
			can.create_oval(10,10,180,180,fill="red")
		else:
			can.create_oval(10,10,180,180)



vars = StringVar()
r1 = Radiobutton(w,text="Rectangle",variable=vars,value="rect",command=draw)
r2 = Radiobutton(w,text="Oval",variable=vars,value="oval",command=draw)

varf = IntVar()
c1 = Checkbutton(w,text="Filled",variable=varf,onvalue=1,offvalue=0,command=draw)



can.pack()
r1.pack()
r2.pack()
c1.pack()

w.mainloop()