'''
TkWanderer Game view funcions
'''

from tkinter import *
from PIL import Image, ImageTk

class GameDisplay:

    def __init__(self):
        self.root = Tk()

    def create_canvas(self, area_floorplan): # > control init calls it
        self.canvas_dimensions = [len(area_floorplan), len(area_floorplan[0])] # area rows, area columns

        self.tile_width = 72

        self.canvas = Canvas(self.root, width=self.canvas_dimensions[1]*self.tile_width,       height=self.canvas_dimensions[0]*self.tile_width)
        self.canvas.pack()

    def display_area(self, area_floorplan):

        select_tile_pattern_display_call = { '0': self.display_floor, '1': self.display_wall}

        for row in range(self.canvas_dimensions[0]):
            for column in range(self.canvas_dimensions[1]):
                select_tile_pattern_display_call[area_floorplan[row][column]]([column*self.tile_width, row*self.tile_width])

    def display_floor(self, tile_position):
        floor_image = PhotoImage(file='./img/floor.png')
        self.canvas.create_image(tile_position[0], tile_position[1], anchor=NW, image=floor_image)

    def display_wall(self, tile_position):
        wall_image = PhotoImage(file='./img/wall.png')
        self.canvas.create_image(tile_position[0], tile_position[1], anchor=NW, image=wall_image)

    def put_all_in_mainloop(self):
        mainloop()

    def display_hero(self, hero_position):
        hero_image = PhotoImage(file='./img/hero-down.png')
        self.canvas.create_image(hero_position[0], hero_position[1], anchor=NW, image=hero_image)
