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
        self.view = view.GameDisplay(self.model.get_area_floorplan())
        self.hero = model.Hero()

        self.game_flow_controller()

    def game_flow_controller(self):
        # Init level
        #   Character generation < Model char data
        # Launch level (=tkinter loop)
        self.game_display_controller()

            # Starting position display
        # Main loop:
            # Get I/O
            # Move characters
            # Check positions
            # Check if battle > Call battle
            # Display

    def game_display_controller(self):
        self.view.display_loop()
        # display enemies


# LAUNCH GAME
game = Game()
