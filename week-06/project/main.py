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
        self.is_game_running = True
        # Launch level (=tkinter loop)

        # *** [ Main loop: ] ***
        while self.is_game_running:
            self.game_area_phase_display() # Draws everything
            self.game_keyboard_listener() # Binds kb input and executes commands
                # Process I/O (got via self.view)
                #   Move characters
                #   Check positions
                #   Check if battle > Call battle
        self.view.root.quit()

    def game_area_phase_display(self):
        self.view.clear_canvas()
        self.view.display_area()
        self.view.display_hero(self.hero.get_hero_position())
        
        # TODO: (MEH) Why can't make separate view functions for game objects? (Map, Hero, Enemies)
        # TODO: display enemies

    def game_keyboard_listener(self):
        self.view.root.bind('<Key>', self.game_keyboard_interpreter)

    def game_keyboard_interpreter(self, event):
        print('Key pressed is', event.keysym) # NOTE Test only
        command_interpretation = {'Down': self.hero.set_hero_postion, 'q': self.game_command_interpreter}
        command_interpretation[event.keysym](event.keysym)

    def game_command_interpreter(self, keyboard_input):
        if keyboard_input == 'q':
            print('You can run but you cannot hide.')
            self.is_game_running = False




# LAUNCH GAME
game = Game()
