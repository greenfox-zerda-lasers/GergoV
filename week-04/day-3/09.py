# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

from tkinter import *

root = Tk()
canvas = Canvas(root, width="300", height="300", bg="lightgray")
canvas.pack()

def origorect(d):
    canvas.create_rectangle(150 - d/2, 150 - d/2, 150 + d/2, 150 + d/2)

origorect(20)
origorect(100)
origorect(80)

root.mainloop()
