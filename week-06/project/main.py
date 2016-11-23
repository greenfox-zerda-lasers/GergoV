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
        self.hero = model.Hero()
        self.view = view.GameDisplay(self.model.get_area_floorplan())

        self.game_flow_controller()

    def game_flow_controller(self):
        # Init level
        #   Character generation < Model char data
        # Launch level (=tkinter loop)
        self.game_display_level_phase()

            # Starting position display
        # Main loop:
            # Process I/O (got via self.view)
            #   Move characters
            #   Check positions
            #   Check if battle > Call battle

    def game_display_level_phase(self):
        self.view.display_loop(self.hero.get_hero_position())
        # TODO: Why can't make separate view functions for game objects? (Map, Hero, Enemies)
        # TODO: display enemies

    def move_hero_down(self):
        self.hero.set_hero_postion('down')


# LAUNCH GAME
game = Game()
