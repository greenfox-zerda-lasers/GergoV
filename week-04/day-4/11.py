# Yellow fractal #FEFB00

from tkinter import *

root = Tk()

w = 600
split = 3

canvas = Canvas(root, width=w, height=w, bg="#FEFB00")
canvas.pack()

def rectangle(x, y, w):
    canvas.create_rectangle(x, y, x+w, y+w)

def rect_fractal(x, y, w):
    rectangle(x, y, w)
    if w > 5:
        rect_fractal(x, y+w/split, w/split)
        rect_fractal(x+(w*(2/split)), y+w/split, w/split)
        rect_fractal(x+w/split,y,w/split)
        rect_fractal(x+w/split,y+(w*(2/split)), w/split)

rect_fractal(0, 0, 600)

mainloop()
