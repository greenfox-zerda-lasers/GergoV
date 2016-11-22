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
        # instantiate model and view
        # set ActiveArea paramteres
        # generate level map model < get map data < generate characters
        # instantiate ActiveArea
