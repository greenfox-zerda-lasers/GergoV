'''
TkWanderer Game view funcions
'''

from tkinter import *
from PIL import Image, ImageTk

class GameDisplay:

    def __init__(self, area_floorplan):
        self.area_floorplan = area_floorplan
        self.canvas_dimensions = [len(self.area_floorplan), len(self.area_floorplan[0])]
        self.tile_width = 72

        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.canvas_dimensions[1]*self.tile_width,       height=self.canvas_dimensions[0]*self.tile_width)
        self.canvas.pack()

    def key_move_down(self, event):
        # TODO: check event.keysym; move this to controller
        pass

    def display_loop(self, hero_position):

        # Display background:
        floor_image = PhotoImage(file='./img/floor.png')
        wall_image = PhotoImage(file='./img/wall.png')
        select_tile_pattern_display = {'0': floor_image, '1': wall_image}

        for row in range(self.canvas_dimensions[0]):
            for column in range(self.canvas_dimensions[1]):
                self.canvas.create_image(column*self.tile_width, row*self.tile_width, anchor=NW, image=select_tile_pattern_display[self.area_floorplan[row][column]])

        # Display hero:
        hero_image = PhotoImage(file='./img/hero-down.png')
        self.canvas.create_image(hero_position[0], hero_position[1], anchor=NW, image=hero_image)

        # Listen keyboard input
        # TODO: self.root.bind('<KeyPress>', self.key_move_down) - bind this to root in control

        self.root.mainloop()
