# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

# create a 300x300 canvas.

from tkinter import *

root = Tk()
canvas = Canvas(root, width="300", height="300")
canvas.pack()

def tocenter(x, y):
    canvas.create_line(x, y, 300/2, 300/2)

for i in range(0, 300, 20):
    tocenter(i, 0)
    tocenter(300, i)
    tocenter(i, 300)
    tocenter(0, i)


root.mainloop()
