# create a 300x300 canvas.
# draw a green 10x10 square to its center.

from tkinter import *

root = Tk()

w = 300
h = 300

canvas = Canvas(root, width=w, height=h)
canvas.pack()

canvas.create_rectangle(w/2-5, h/2+5, w/2+5, h/2-5, fill="lime")

mainloop()
