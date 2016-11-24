'''
TkWanderer Game view funcions
'''

from tkinter import *
from PIL import Image, ImageTk

class LevelDisplay:

    def __init__(self, area_dimensions):

        # Init area variables:
        self.tile_width = 72

        # Init canvas:
        self.root = Tk()
        self.canvas = Canvas(self.root, width=area_dimensions[1]*self.tile_width,       height=area_dimensions[0]*self.tile_width)
        self.canvas.pack()

        # Init imagery:
        self.floor_image = PhotoImage(file='./img/floor.png')
        self.wall_image = PhotoImage(file='./img/wall.png')
        self.hero_image = PhotoImage(file='./img/hero-down.png')

        self.hero_down = PhotoImage(file='./img/hero-down.png')
        self.hero_up = PhotoImage(file='./img/hero-up.png')
        self.hero_left = PhotoImage(file='./img/hero-left.png')
        self.hero_right = PhotoImage(file='./img/hero-right.png')

        self.boss = PhotoImage(file='./img/boss.png')
        self.skeleton = PhotoImage(file='./img/skeleton.png')


    # *** [ Display functions in tkinter mainloop ] ***

    def display_area(self, area_dimensions, area_floorplan):
        select_tile_pattern_display = {'0': self.floor_image, '1': self.wall_image}

        for row in range(area_dimensions[0]):
            for column in range(area_dimensions[1]):
                self.canvas.create_image(column*self.tile_width, row*self.tile_width, anchor=NW, image=select_tile_pattern_display[area_floorplan[row][column]])

    def display_hero(self, hero_position, heading):
        if heading == "Up":
            hero_heading_image = self.hero_up
        if heading == "Down":
            hero_heading_image = self.hero_down
        if heading == "Left":
            hero_heading_image = self.hero_left
        if heading == "Right":
            hero_heading_image = self.hero_right
        self.canvas.create_image(hero_position[0]*self.tile_width, hero_position[1]*self.tile_width, anchor=NW, image=hero_heading_image)

    def display_enemies(self, enemy_type, enemy_position):
        if enemy_type == 'Boss':
            enemy_view_image = self.boss
        if enemy_type == 'Skeleton':
            enemy_view_image = self.skeleton

        self.canvas.create_image(enemy_position[0]*self.tile_width, enemy_position[1]*self.tile_width, anchor=NW, image=enemy_view_image)



    # *** [ View control funcions ] ***
    def clear_canvas(self):
        self.canvas.delete('all')

    def canvas_update(self):
        self.canvas.update()

    def show(self):
        self.root.mainloop()
