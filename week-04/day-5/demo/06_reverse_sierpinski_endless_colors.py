# Reverse Sierpinski triangle
# Triangles are equilateral, so triangle height (h) is:
# a * sqr(0,75), or a * 0,866

from tkinter import *

root = Tk()
w = 667
h = 0.866
canvas = Canvas(root, width=w, height=w*h, bg="black")
canvas.pack()

def draw_eq_triangle(x, y, a, line_color):

    topleft = x, y
    topright = x + a, y
    bottom = x + (1/2 * a), y + (a * h)

    canvas.create_polygon(topleft, topright, bottom, fill='black', outline=line_color)

def reverse_sierpinski(x, y, a, fractal_color, depth):
    draw_eq_triangle(x, y, a, fractal_color)
    if a > depth:
        reverse_sierpinski(x, y, a/2, fractal_color, depth)
        reverse_sierpinski(x + a/2, y, a/2, fractal_color, depth)
        reverse_sierpinski(x + a/4, y + a/2 * h, a/2, fractal_color, depth)
        #reverse_sierpinski(x + a*(3/8), y + (a/4 * h), a/4, fractal_color, depth)

# animation and coloring
scale = 1
color = 100
fractal_w = 100

for i in range(1, 3000):
    fractal_w += 200
    if fractal_w > 2*w:
        fractal_w = w
        canvas.update()

    color += 20
    if scale == 6:
        scale = 1
    if color >= 256:
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

    reverse_sierpinski(0, 0, fractal_w, level_color, 30)
    # print(fractal_w)
    canvas.update()

root.mainloop()
