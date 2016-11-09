
# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *

root = Tk()
canvas = Canvas(root, width="300", height="300", bg="lightgray")
canvas.pack()

for i in range(7):
    d = 20
    steps = 5
    canvas.create_rectangle(150 - d/2 * steps * i, 150 - d/2, 150 + d/2, 150 + d/2)


root.mainloop()
