from tkinter import *
from PIL import Image, ImageTk

root = Tk()
canvas = Canvas(root)

tile_image = Image.open('../img/floor.gif')
tile_photo = ImageTk.PhotoImage(tile_image)

for r in range(2):
    for c in range(2):
        label = Label(image=tile_photo)
        label.tile_image = tile_photo # keep a reference!
        label.grid(row=r, column=c)

hero_image = Image.open('../img/hero-down.gif')
hero_photo = ImageTk.PhotoImage(hero_image)

label2 = Label(image=hero_photo)
label2.hero_image = hero_photo
canvas.tag_raise(label2)
label2.grid(row=0, column=0)

canvas.lift(label2)



root.mainloop()
