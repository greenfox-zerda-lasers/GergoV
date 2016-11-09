# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

root = Tk()
canvas = Canvas(root, width="300", height="300")
canvas.pack()

canvas.create_rectangle(0, 0, 120, 150, fill="lime")
canvas.create_rectangle(125, 4, 220, 73, fill="yellow")
canvas.create_rectangle(4, 160, 160, 230, fill="red")
canvas.create_rectangle(170, 80, 290, 293, fill="cyan")

root.mainloop()
