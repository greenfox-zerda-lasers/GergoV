# Reverse Sierpinski triangle
# Triangles are equilateral, so triangle height (h) is:
# a * sqr(0,75), or a * 0,866

from tkinter import *

root = Tk()
w = 667
h = 0.866
canvas = Canvas(root, width=w, height=w*h, bg="lightgray")
canvas.pack()

def reverse_sierpinski(x, y, a):

    triangle_a_topleft = x, y # upper left corner
    triangle_a_topright = x + (1/2 * a), y
    triangle_a_bottom = x + (1/4 * a), y + ((1/2 * a) * h)

    triangle_b_topleft = triangle_a_topright
    triangle_b_topright = x + a, y
    triangle_b_bottom = x + (3/4 * a), y + ((1/2 * a) * h)

    triangle_c_topleft = triangle_a_bottom
    triangle_c_topright = triangle_b_bottom
    triangle_c_bottom = x + (1/2 * a), y + (a * h) # bottom pike


    canvas.create_polygon(triangle_a_topleft, triangle_a_topright, triangle_a_bottom, fill='white', outline='black')
    #canvas.create_polygon(triangle_b_topleft, triangle_b_topright, triangle_b_bottom, fill='white', outline='black')
    #canvas.create_polygon(triangle_c_topleft, triangle_c_topright, triangle_c_bottom, fill='white', outline='black')

    if a > 20:
            reverse_sierpinski(x, y, a/2)
            reverse_sierpinski(x + a/2, y, a/2)
            reverse_sierpinski(x + a/4, y + a/2 * h, a/2)


reverse_sierpinski(30, 10, 600)

root.mainloop()
