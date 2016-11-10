from tkinter import *

root = Tk()
canvas = Canvas(root, width="300", height="300", bg="white")
canvas.pack()

startpos = 0
endpos = 0
dist = 10

for i in range(1, 6):
    prevboxes = 0
    for j in range(1, i):
        prevboxes += dist * j
    startpos = dist + prevboxes
    endpos = startpos + (dist * i)
    canvas.create_rectangle(startpos, startpos, endpos, endpos, fill="#b145f3")

root.mainloop()
