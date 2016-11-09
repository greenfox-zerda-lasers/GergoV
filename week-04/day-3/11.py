
# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *

root = Tk()
w = 300
h = 300
canvas = Canvas(root, width=w, height=h, bg="lightgray")
canvas.pack()


def origorect(d, color):
    origox = w/2
    origoy = h/2
    tlx = origox - d/2
    tly = origoy - d/2
    lrx = origox + d/2
    lry = origox + d/2

    rainbow_colors = ["red", "orange", "yellow", "green", "blue", "cyan", "violet"]

    steps = (origox - d/2) / 7


    for i in range(7, 0, -1):
        dist = steps * i
        canvas.create_rectangle(tlx - dist, tly - dist, lrx + dist, lry + dist, fill=rainbow_colors[i-1])
        print(dist)

    canvas.create_rectangle(tlx, tly, lrx, lry, fill=color)


origorect(80, "lime")

root.mainloop()
