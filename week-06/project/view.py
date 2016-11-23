'''
TkWanderer Game view funcions
'''

from tkinter import *
from PIL import Image, ImageTk

class GameDisplay:

    def __init__(self):
        self.root = Tk()

    def create_canvas(self, area_floorplan):
        self.canvas_dimensions = [len(area_floorplan), len(area_floorplan[0])] # area rows, area columns

        self.tile_width = 72

        self.canvas = Canvas(self.root, width=self.canvas_dimensions[1]*self.tile_width,       height=self.canvas_dimensions[0]*self.tile_width)
        self.canvas.pack()

        return self.canvas_dimensions, self.tile_width

    def display_area(self, area_floorplan):

        floor_image = PhotoImage(file='./img/floor.png')
        wall_image = PhotoImage(file='./img/wall.png')
        select_tile_pattern_display = {'0': floor_image, '1': wall_image}

        for row in range(self.canvas_dimensions[0]):
            for column in range(self.canvas_dimensions[1]):
                self.canvas.create_image(column*self.tile_width, row*self.tile_width, anchor=NW, image=select_tile_pattern_display[area_floorplan[row][column]])

        mainloop()

    def put_all_in_mainloop(self):
        mainloop()

    def display_hero(self, hero_position):
        hero_image = PhotoImage(file='./img/hero-down.png')
        self.canvas.create_image(hero_position[0], hero_position[1], anchor=NW, image=hero_image)

        mainloop()
