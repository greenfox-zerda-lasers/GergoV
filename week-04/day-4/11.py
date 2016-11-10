# Yellow fractal #FEFB00

from tkinter import *

root = Tk()

w = 600

canvas = Canvas(root, width=w, height=w, bg="#FEFB00")
canvas.pack()

n = 3
depth = 6
steps = n**2

# draw main layout
for i in range(0, n):
    for j in range (0, n):
        for k in range (0, n):
            canvas.create_rectangle((w/n)*j, (w/n)*i, (w/n)*(j+1), (w/n)*(i+1))



mainloop()
