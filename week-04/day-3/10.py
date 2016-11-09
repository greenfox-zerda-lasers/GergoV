# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *

root = Tk()
canvas = Canvas(root, width="300", height="300", bg="lightgray")
canvas.pack()

def origorect(d):
    canvas.create_rectangle(150 - d/2, 150 - d/2, 150 + d/2, 150 + d/2)

for i in range(1, 100, 5):
    origorect(80 + i)

root.mainloop()
