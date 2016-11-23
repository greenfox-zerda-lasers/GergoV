'''
TkWanderer Game view funcions
'''

from tkinter import *
from PIL import Image, ImageTk

class GameDisplay:

    def __init__(self):
        pass

    def display_area(self):
        self.root = Tk()

        # Get tile images for measuring
        tile_image = PhotoImage(file="./img/floor.png")
        tile_width = tile_image.width()

        # Canvas config
        canvas_rows = 11
        canvas_columns = 10

        canvas = Canvas(self.root, width=canvas_columns*tile_width, height=canvas_rows*tile_width)

        # Display tiles
        for row in range(11):
            for column in range(10):
                canvas.create_image(column*tile_width, row*tile_width, anchor=NW, image=tile_image)

        canvas.pack()
        mainloop()
