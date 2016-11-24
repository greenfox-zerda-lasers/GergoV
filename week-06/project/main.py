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

        # *** [ Movement variables ]
        self.hero_heading = 'Down'
        self.movement_alterations = {'Up':[0, -1], 'Down':[0, 1], 'Left':[-1, 0], 'Right':[1, 0]}

        self.game_flow_controller()

    def game_flow_controller(self):
        # TODO: Init level

        # *** [ TKinter Main loop: ] ***
        self.game_phase_display() # Draws everything
        self.game_keyboard_listener() # Binds kb input and executes commands
        self.view.show()

# *** [ Game View Controller Functions ] ***

    def game_phase_display(self):
        self.view.clear_canvas() # NOTE: Works without cleaning too. Maybe this spares memory?
        self.view.display_area()
        self.view.display_hero(self.hero.get_hero_position(), self.hero_heading)
        # TODO: display enemies

# *** [ Game keyboard IO] ***

    def game_keyboard_listener(self):
        self.view.root.bind('<Key>', self.game_command_interpreter)
        # NOTE: Later may need interpreter for other key commands.

    def game_command_interpreter(self, event):
        key_pressed = event.keysym
        movement_keys = ['Up', 'Down', 'Left', 'Right']
        actions_keys = ['space', 'q']
        if key_pressed in movement_keys:
            self.turn_and_move_hero(key_pressed)
        elif key_pressed in actions_keys:
            print('Command:', key_pressed)
        else:
            print('Invalid command:', key_pressed) # NOTE: Indev.

# *** [ Character movement ] ***

    def turn_and_move_hero(self, direction):
        self.hero_heading = direction # NOTE: Not writing back to model (hero object).
        # self.detect_collision()
        self.hero.set_hero_postion(self.movement_alterations[direction])
        self.game_phase_display()

    def detect_collision():
        pass


# *** [ LAUNCH GAME ] ***
main = Game()
