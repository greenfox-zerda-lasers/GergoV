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
        # TODO: Init level

        # *** [ TKinter Main loop: ] ***
        self.game_phase_display() # Draws everything
        self.game_keyboard_listener() # Binds kb input and executes commands
        self.view.show()

# *** [ Game View Controller Functions ] ***

    def game_phase_display(self):
        self.view.clear_canvas()
        self.view.display_area()
        self.view.display_hero(self.hero.get_hero_position())
        # TODO: display enemies

# *** [ Game keyboard IO] ***

    def game_keyboard_listener(self):
        self.view.root.bind('<Key>', self.move_hero)

    def move_hero(self, event):
        self.hero.set_hero_postion(event.keysym)
        self.game_phase_display()

# LAUNCH GAME
main = Game()
