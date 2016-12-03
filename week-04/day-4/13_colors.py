# Hexagonal fractal 2: 3 hexagons inside
# + Random colors +Endless main loop

from tkinter import *
import random
import time

root = Tk()
w = 696 # height = 545
h = 0.866
canvas = Canvas(root, width=w, height=545, bg="lightgray")
canvas.pack()

def draw_hexagon(x, y, a, fill_color):

    topleft = x, y
    topright = x + a, y
    right = x + (1.5 * a), y + (a * h)
    bottomright = x + a, y + 2 * (a * h)
    bottomleft = x, y + 2 * (a * h)
    left = x - a/2, y + (a * h)

    canvas.create_polygon(topleft, topright, right, bottomright, bottomleft, left, fill=fill_color, outline='black')

def hexagonal_fractal(x, y, a, depth):

    col_r = random.randrange(255)
    col_g = random.randrange(255)
    col_b = random.randrange(255)

    fill_color = '#%02x%02x%02x' % (col_r, col_g, col_b)

    draw_hexagon(x, y, a, fill_color)
    if a > depth:
        a = a/2
        hexagonal_fractal(x, y, a, depth)
        hexagonal_fractal(x + (1.5 * a), y + (a * h), a, depth)
        hexagonal_fractal(x, y + 2 * (a * h), a, depth)
    time.sleep(0.001)
    canvas.update()

i = 1
while i == 1:
    hexagonal_fractal(200, 10, 300, 10)

root.mainloop()
