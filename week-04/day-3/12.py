
# create a 300x300 canvas.
# fill it with a checkerboard pattern.


from tkinter import *

root = Tk()
canvas = Canvas(root, width="300", height="300", bg="black")
canvas.pack()

counter = 0

for i in range(1, 9):
    for j in range(1, 9):
        if counter % 2 != 0:
            sqcolor="white"
        if counter % 2 == 0:
            sqcolor="green"
        tlx = (300 / 8) * (j - 1)
        tly = (300 / 8) * (i - 1)
        brx = (300 / 8) * (j + 2)
        bry = (300 / 8) * (i + 2)

        canvas.create_rectangle(tlx, tly, brx, bry, fill=sqcolor)
        counter += 1
    counter += 1

mainloop()
