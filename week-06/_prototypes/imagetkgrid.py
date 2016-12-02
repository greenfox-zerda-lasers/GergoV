from tkinter import *
from PIL import Image, ImageTk


root = Tk()

image = Image.open('../img/floor.gif')
photo = ImageTk.PhotoImage(image)

label = Label(image=photo)
label.image = photo # keep a reference!
label.grid(row=0, column=1)

image = Image.open('../img/boss.gif')
photo = ImageTk.PhotoImage(image)

label = Label(image=photo)
label.image = photo # keep a reference!
label.grid(row=0, column=2)

mainloop()
