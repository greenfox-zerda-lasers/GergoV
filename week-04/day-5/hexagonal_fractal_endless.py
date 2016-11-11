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

def draw_hexagon(x, y, a):

    topleft = x, y
    topright = x + a, y
    right = x + (1.5 * a), y + (a * h)
    bottomright = x + a, y + 2 * (a * h)
    bottomleft = x, y + 2 * (a * h)
    left = x - a/2, y + (a * h)

    canvas.create_polygon(topleft, topright, right, bottomright, bottomleft, left, fill='white', outline='black')

def hexagonal_fractal(x, y, a, depth):
    draw_hexagon(x, y, a)
    if a > depth:
        a = a/3
        hexagonal_fractal(x, y, a, depth)
        hexagonal_fractal(x + 2*(a), y, a, depth)
        hexagonal_fractal(x + 3 * a, y + 2 * a * h, a, depth)
        hexagonal_fractal(x + 2*(a), y + 2* 2 * a * h, a, depth)
        hexagonal_fractal(x, y + 2* 2 * a * h, a, depth)
        hexagonal_fractal(x - a, y + 2 * a * h, a, depth)

for i in range(1, 100):
    hexagonal_fractal(200 - i, 10 - i, 300 + i, 5)
    time.sleep(0.000000000001)

    canvas.update()

root.mainloop()
