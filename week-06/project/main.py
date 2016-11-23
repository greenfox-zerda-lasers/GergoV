'''
*** TkWanderer Game ***
by Gergo Vamosi, alias GergoV

Green Fox Academy, 2016.
'''

import model
import view

class Game:
    '''
    Game controller object with main game functions.
    '''

    def __init__(self):
        self.model = model.GameData()
        self.view = view.GameDisplay()
        self.hero = model.Hero()

        self.game_flow_controller()

    def game_flow_controller(self):
        # Init level
        #   Character generation < Model char data
        # Launch level
        self.init_level_display()
        self.game_display_controller()

            # Starting position display
        # Main loop:
            # Get I/O
            # Move characters
            # Check positions
            # Check if battle > Call battle
            # Display

    def init_level_display(self):
        self.view.create_canvas(self.model.get_area_floorplan())
        # generate characters < model char data, model level data

    def game_display_controller(self):
        self.view.display_area(self.model.get_area_floorplan())
        self.view.display_hero(self.hero.get_hero_position())
        # display enemies


# LAUNCH GAME
game = Game()
