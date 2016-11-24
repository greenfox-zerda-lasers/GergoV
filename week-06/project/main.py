'''
*** TkWanderer Game ***
Version 1.0
by Gergo Vamosi, alias GergoV
https://github.com/GergoV

Green Fox Academy, Zerda class, Lasers group, 2016.
'''

import model
import view

class Game:
    '''
    Game controller object with main game functions.
    '''

    def __init__(self):
        self.model = model.AreaMap()
        self.hero = model.Hero()

        # *** [ Movement variables, rulesets ] ***
        # TODO: Store them better.
        self.hero_heading = 'Down'
        self.movement_alterations = {'Up':[0, -1], 'Down':[0, 1], 'Left':[-1, 0], 'Right':[1, 0]}

        self.game_flow_controller()

    def game_flow_controller(self):
        self.init_level()

        # *** [ TKinter Main loop: ] ***
        self.game_phase_display() # Draws everything
        self.game_keyboard_listener() # Binds kb input and executes commands
        self.view.show()


    def init_level(self):
        self.area_dimensions = self.model.get_area_dimensions()
        self.area_floorplan = self.model.get_area_floorplan()

        self.view = view.LevelDisplay(self.area_dimensions)

# *** [ Game View Controller Functions ] ***

    def game_phase_display(self):
        self.view.clear_canvas() # NOTE: Works without cleaning too. Maybe this spares memory?
        self.view.display_area(self.area_dimensions, self.area_floorplan)
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
            print('Command:', key_pressed) # NOTE: Indev
        else:
            print('Invalid command:', key_pressed) # NOTE: Indev.

# *** [ Character movement ] ***

    def turn_and_move_hero(self, direction):
        self.hero_heading = direction # NOTE: Not writing back to model (hero object). Only view needs it.
        if self.is_way_free(direction) == True:
            self.hero.set_hero_position(self.movement_alterations[direction])
        else:
            print("BANG!")
        self.game_phase_display()

    def is_way_free(self, direction):
        # All data is read from model via level init.
        target_position = [0, 0] # NOTE: x, y = column, row
        map_max_x = range(self.area_dimensions[1])
        map_max_y = range(self.area_dimensions[0])
        # NOTE: Resolved only for easier overview and debugging

        target_position[0] = self.movement_alterations[direction][0] + self.hero.get_hero_position()[0]
        target_position[1] = self.movement_alterations[direction][1] + self.hero.get_hero_position()[1]

        if target_position[0] in map_max_x and target_position[1] in map_max_y:
            target_tile_type = int(self.area_floorplan[target_position[1]][target_position[0]])
            # NOTE: ^IDK why it becomes str.
            print(target_tile_type)
            if target_tile_type < 1:
                return True
            else:
                return False



# *** [ LAUNCH GAME ] ***
main = Game()
