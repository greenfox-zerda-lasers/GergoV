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
        self.model = model.GameData
        self.view = view.GameDisplay

        self.display_active_area()

    def display_active_area(self):
        self.view.display_area(self, self.model.get_area_floorplan(self))

# LAUNCH GAME
game = Game()
