from tkinter import *

root = Tk()
canvas = Canvas(root, width="300", height="300", bg="white")
canvas.pack()

for i in range(1, 20):
    dist = 10
    canvas.create_rectangle(dist*i, dist*i, dist + dist*i, dist + dist*i, fill="#b145f3")

root.mainloop()
