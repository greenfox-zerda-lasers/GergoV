# Reverse Sierpinski triangle
# Triangles are equilateral, so triangle height (h) is:
# a * sqr(0,75), or a * 0,866

from tkinter import *
import time

root = Tk()
w = 667
h = 0.866
canvas = Canvas(root, width=w, height=w*h, bg="lightgray")
canvas.pack()

root.geometry("667x580+50+50")

def reverse_sierpinski(x, y, a):

    topleft = x, y
    topright = x + a, y
    bottom = x + (1/2 * a), y + (a * h)

    canvas.create_polygon(topleft, topright, bottom, fill='white', outline='black')

    if a > 10:
        reverse_sierpinski(x, y, a/2)
        reverse_sierpinski(x + a/2, y, a/2)
        reverse_sierpinski(x + a/4, y + a/2 * h, a/2)

        time.sleep(0.005)
        canvas.update()

reverse_sierpinski(30, 10, 600)



root.mainloop()
