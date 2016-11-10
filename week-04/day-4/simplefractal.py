from tkinter import *
root = Tk()

w = 600
split = 3

canvas = Canvas(root, width=w, height=w, bg="#1A5325")
canvas.pack()

def rectangle(x, y, w):
    canvas.create_rectangle(x, y, x+w, y+w)
    if w > 5:
        rectangle(x, y+w/split, w/split)
        rectangle(x+(w*(2/split)), y+w/split, w/split)
        rectangle(x+w/split,y,w/split)
        rectangle(x+w/split,y+(w*(2/split)), w/split)

rectangle(0,0,600)

root.mainloop()
