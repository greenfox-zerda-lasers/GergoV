"""
*** Mini Maze Game ***

 Player has to find treasure in a maze.
 Maze is composed of rooms; each room has a different wall type, dampness and
 lighting as a quality and exits to certain directions.
 Treasure is either in the room or not.
"""

class Room():

    def __init__(self, room_posx, room_posy, room_exits, room_has_treasure):
        self.room_posx = room_posx
        self.room_posy = room_posy
        self.room_exits = room_exits # list of integers, n-e-s-w order, 0 or 1
        self.room_has_treasure = room_has_treasure

# Room Type: Entrance, Treasure room
# 3 qualities to descript
# exit directions

class MoveAround():
# generate room
#   check pos
#   tell exits
# ask move
#   input
#   check input vs. room
#   Move north, south, east, west. - pos + move

    def __init__(self):
        self.player_posx = 1
        self.player_posy = 1

        # Start MAIN LOOP
        self.startgame()

    #def generate_room(self, self.player_posx, self.player_posy):
    #    pass

    def input_move(self):
        self.player_movex = 0
        self.player_movey = 0
        direction = input()
        if direction == "north":
            self.player_movex = 1
        if direction == "east":
            self.player_movey = 1
        if direction == "west":
            self.player_movey = -1
        if direction == "south":
            self.player_movey = -1
        if direction == "q":
            self.quitgame()
        else:
            print("Please enter valid direction or q to quit!")
        return self.player_movex, self.player_movey

    def move_player(self):
        self.player_posx += self.player_movex
        self.player_posy += self.player_movey

        print("You are in position %d, %d on the map." % (self.player_posx, self.player_posy))

    def startgame(self):
        self.is_running = 1
        print("The game is starting!\n")
        self.game_loop()

    def quitgame(self):
        self.is_running = 0


    def game_loop(self):
        while self.is_running == 1:
            print("Enter a direction to move around on map or press q to quit!")
            self.input_move()
            self.move_player()
        print("\nThe game has ended!\n" + "Thank you for playing! Bye!")

room_1 = Room(1, 1, [0, 1, 0, 0], 0)
room_2 = Room(1, 1, [0, 1, 0, 0], 0)
room_3 = Room(1, 1, [0, 1, 0, 0], 1)
walkaround = MoveAround()
# walkaround.startgame()
