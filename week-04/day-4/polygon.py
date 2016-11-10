# Yellow fractal #FEFB00

from tkinter import *

root = Tk()
w = 611
canvas = Canvas(root, width=w, height=w)
canvas.pack()

canvas.create_polygon(w/3,w/3, (w/3)*2,w/3, w/2,(w/3)*2, fill="red")
canvas.create_polygon(w/3,w/3, (w/3)*2,w/3, w/2,(w/3)*2, fill="red")



mainloop()
