# meh

import tkinter as tk

m = tk.Tk()

canvas = tk.Canvas(m, width=300, height=300)
canvas.pack()

img = tk.PhotoImage(file="floor.gif")
canvas.create_image(20,20, anchor=NW, image=img)

m.mainloop()
