# Game view prototype

from tkinter import *
from PIL import Image, ImageTk # Neen PIL for png

root = Tk()

# Get tile images for measuring
tile_image = PhotoImage(file="../img/floor.png")
tile_width = tile_image.width()

# Canvas config
canvas_rows = 11
canvas_columns = 10

canvas = Canvas(root, width=canvas_columns*tile_width, height=canvas_rows*tile_width)

# Display tiles

for row in range(11):
    for column in range(10):
        canvas.create_image(column*tile_width, row*tile_width, anchor=NW, image=tile_image)


canvas.pack()
mainloop()
