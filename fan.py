from tkinter import *
import random

root = Tk()
canvas = Canvas(root, width=400, height=400)
#encloses circle in bound rectangle
bound = 50, 50, 300, 300
#draws 30degree arcs from angles 0, 90, 180, 270
c = ["red","green","blue","magenta"]
for i in [0, 90, 180, 270]:
	canvas.create_arc(bound, start=i, extent=30, fill=random.choice(c))
canvas.pack()
root.mainloop()
