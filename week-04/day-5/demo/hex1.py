# Hexagonal fractal
# Remember, a hexagon is 6 equlateral triangles, so
# (Regarding that Eq. triangle height (h) is: a * sqr(0,75), or a * 0,866):

from tkinter import *

root = Tk()
w = 696 # height = 545
h = 0.866
canvas = Canvas(root, width=w, height=545, bg="lightgray")
canvas.pack()

def hexagonal_fractal(x, y, a):

    topleft = x, y
    topright = x + a, y
    right = x + (1.5 * a), y + (a * h)
    bottomright = x + a, y + 2 * (a * h)
    bottomleft = x, y + 2 * (a * h)
    left = x - a/2, y + (a * h)

    canvas.create_polygon(topleft, topright, right, bottomright, bottomleft, left, fill='white', outline='black')

    if a > 5:
        hexagonal_fractal(x, y, a/3)

hexagonal_fractal(200, 10, 300)

root.mainloop()
