'''
TkWanderer Game view funcions
'''

from tkinter import *
from PIL import Image, ImageTk

class GameDisplay:

    def __init__(self, area_floorplan):

        # Init area variables:
        self.area_floorplan = area_floorplan
        self.canvas_dimensions = [len(self.area_floorplan), len(self.area_floorplan[0])]
        self.tile_width = 72

        # Init canvas:
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.canvas_dimensions[1]*self.tile_width,       height=self.canvas_dimensions[0]*self.tile_width)
        self.canvas.pack()

        # Init imagery:
        self.floor_image = PhotoImage(file='./img/floor.png')
        self.wall_image = PhotoImage(file='./img/wall.png')
        self.hero_image = PhotoImage(file='./img/hero-down.png')


    def display_area(self):

        select_tile_pattern_display = {'0': self.floor_image, '1': self.wall_image}

        for row in range(self.canvas_dimensions[0]):
            for column in range(self.canvas_dimensions[1]):
                self.canvas.create_image(column*self.tile_width, row*self.tile_width, anchor=NW, image=select_tile_pattern_display[self.area_floorplan[row][column]])

    def display_hero(self, hero_position):
        self.canvas.create_image(hero_position[0], hero_position[1], anchor=NW, image=self.hero_image)

    def clear_canvas(self):
        self.canvas.delete('all')

    def show(self):
        self.root.mainloop()
