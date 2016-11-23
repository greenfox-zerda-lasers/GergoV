'''
TkWanderer Game view funcions
'''

from tkinter import *
from PIL import Image, ImageTk

class GameDisplay:

    def __init__(self):
        pass

    def display_area(self, area_floorplan):
        self.root = Tk()

        # Get tile images, measuring
        floor_image = PhotoImage(file='./img/floor.png') # base tile
        wall_image = PhotoImage(file='./img/wall.png')

        tile_width = floor_image.width()

        # Canvas config
        canvas_rows = len(area_floorplan)
        canvas_columns = len(area_floorplan[0])

        canvas = Canvas(self.root, width=canvas_columns*tile_width, height=canvas_rows*tile_width)

        # Display tiles
        floor_pattern = { '0': floor_image, '1': wall_image}

        for row in range(canvas_rows):
            for column in range(canvas_columns):
                canvas.create_image(column*tile_width, row*tile_width, anchor=NW, image=floor_pattern[area_floorplan[row][column]])

        canvas.pack()
        mainloop()
