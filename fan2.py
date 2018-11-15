from tkinter import *

w = Tk()
w.title("Freaky fan")

can = Canvas(w,width=400,height=400)

bound = 50, 50, 300, 300

for i in [75,165,255,345]:
	can.create_arc(bound,start=i,extent=30,fill="yellow")

can.pack()
w.mainloop()