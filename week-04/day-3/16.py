# create a 300x300 canvas.
# make it look like a nigth sky:
# - The background should be black
# - The stars can be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

import random
from tkinter import *

root = Tk()
canvas = Canvas(root, width="300", height="300", bg="black")
canvas.pack()

for i in range(random.randrange(300, 500)):

    size = random.randrange(1, 4)
    x = random.randrange(300)
    y = random.randrange(300)
    col = random.randrange(0, 256)

    starcolor = '#%02x%02x%02x' % (col, col, col)

    canvas.create_rectangle(x, y, x+size, y+size, fill=starcolor)


root.mainloop()
