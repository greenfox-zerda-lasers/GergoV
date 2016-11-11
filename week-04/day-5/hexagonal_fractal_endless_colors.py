# Hexagonal fractal
# Remember, a hexagon is 6 equlateral triangles, so
# (Regarding that Eq. triangle height (h) is: a * sqr(0,75), or a * 0,866):

from tkinter import *
import time

root = Tk()
w = 696 # height = 545
h = 0.866
canvas = Canvas(root, width=w, height=545, bg="black")
canvas.pack()

def draw_hexagon(x, y, a, line_color):

    topleft = x, y
    topright = x + a, y
    right = x + (1.5 * a), y + (a * h)
    bottomright = x + a, y + 2 * (a * h)
    bottomleft = x, y + 2 * (a * h)
    left = x - a/2, y + (a * h)

    canvas.create_polygon(topleft, topright, right, bottomright, bottomleft, left, fill='black', outline=line_color)

def hexagonal_fractal(x, y, a, fractal_color, depth):
    draw_hexagon(x, y, a, fractal_color)
    if a > depth:
        a = a/3
        hexagonal_fractal(x, y, a, fractal_color, depth)
        hexagonal_fractal(x + 2*(a), y, a, fractal_color, depth)
        hexagonal_fractal(x + 3 * a, y + 2 * a * h, a, fractal_color, depth)
        hexagonal_fractal(x + 2*(a), y + 2* 2 * a * h, a, fractal_color, depth)
        hexagonal_fractal(x, y + 2* 2 * a * h, a, fractal_color, depth)
        hexagonal_fractal(x - a, y + 2 * a * h, a, fractal_color, depth)
        hexagonal_fractal(x + a, y + 2 * a * h, a, fractal_color, depth)

# animated version
scale = 1
color = 100

for i in range(1, 3000, 50):
    color += 5
    if scale == 6:
        scale = 1
    if color == 256:
        color = 100
        scale += 1

    if scale == 1:
        col_r = color
        col_g = 0
        col_b = 0
    if scale == 2:
        col_r = 255
        col_g = color
        col_b = 0
    if scale == 3:
        col_r = 0
        col_g = color
        col_b = 0
    if scale == 4:
        col_r = 0
        col_g = 255
        col_b = color
    if scale == 5:
        col_r = 0
        col_g = 0
        col_b = color

    level_color = '#%02x%02x%02x' % (col_r, col_g, col_b)

    hexagonal_fractal(200 - i, 10 - i, 300 + i, level_color, 5)
    canvas.update()


# normal test
# hexagonal_fractal(200, 10, 300, 255, 0, 0, 5)

root.mainloop()
