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

        # run stuff
        self.view.display_area(self)

# LAUNCH GAME
game = Game()
