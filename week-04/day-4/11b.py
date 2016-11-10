# Fractal with loops

from tkinter import *

# root = Tk()
playground = Tk()

w = 600

# canvas = Canvas(root, width=w, height=w, bg="#FEFB00")
canvas2 = Canvas(playground, width=w, height=w, bg="#E3C3B4")

# canvas.pack()
canvas2.pack()

n = 3
depth = 6
steps = n*n

for k in range(1, steps):
    if k % 2 == 0:

        for j in range(1, depth):
            for i in range(1, n):
                canvas2.create_line(i*(w/n), 0, i*(w/n), w) # first line
                canvas2.create_line(0, i*(w/n), w, i*(w/n)) # first line
            w = w / 3

def fractal(n):
    canvas.create_line(w/n, 0, w/n, w) # first line
    canvas.create_line()
    canvas.create_line()
    canvas.create_line()

playground.mainloop()
