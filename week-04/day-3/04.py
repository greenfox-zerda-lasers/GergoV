# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

root = Tk()
canvas = Canvas(width="300", height="300")
canvas.pack()

def drawline(x, y):

    canvas.create_line(x, y, 150, 150, fill="lime")

drawline(20, 20)
drawline(50, 90)
drawline(270, 210)

root.mainloop()
