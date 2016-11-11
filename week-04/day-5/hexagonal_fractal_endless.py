# Hexagonal fractal
# Remember, a hexagon is 6 equlateral triangles, so
# (Regarding that Eq. triangle height (h) is: a * sqr(0,75), or a * 0,866):

from tkinter import *
import time

root = Tk()
w = 696 # height = 545
h = 0.866
canvas = Canvas(root, width=w, height=545, bg="lightgray")
canvas.pack()

def draw_hexagon(x, y, a, col):

    topleft = x, y
    topright = x + a, y
    right = x + (1.5 * a), y + (a * h)
    bottomright = x + a, y + 2 * (a * h)
    bottomleft = x, y + 2 * (a * h)
    left = x - a/2, y + (a * h)

    line_color = starcolor = '#%02x%02x%02x' % (col, col, col)

    canvas.create_polygon(topleft, topright, right, bottomright, bottomleft, left, fill='white', outline=line_color)

def hexagonal_fractal(x, y, a, col, depth):
    draw_hexagon(x, y, a, col)
    if a > depth:
        a = a/3
        hexagonal_fractal(x, y, a, col, depth)
        hexagonal_fractal(x + 2*(a), y, a, col, depth)
        hexagonal_fractal(x + 3 * a, y + 2 * a * h, a, col, depth)
        hexagonal_fractal(x + 2*(a), y + 2* 2 * a * h, a, col, depth)
        hexagonal_fractal(x, y + 2* 2 * a * h, a, col, depth)
        hexagonal_fractal(x - a, y + 2 * a * h, a, col, depth)
        hexagonal_fractal(x + a, y + 2 * a * h, a, col, depth)
"""
for i in range(1, 3000, 20):
    hexagonal_fractal(200 - i, 10 - i, 300 + i, 5)

    canvas.update()
"""
hexagonal_fractal(200, 10, 300, 0, 5)

root.mainloop()
