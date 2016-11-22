import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root)

image = tk.image(open='./floor.gif')
photo = tk.PhotoImage(image)

for r in range(2):
    for c in range(2):
        photo.grid(row=r, column=c)

root.mainloop()
