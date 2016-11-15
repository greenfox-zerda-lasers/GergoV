"""
*** Mini Maze Game ***

 Player has to find treasure in a maze.
 Maze is composed of rooms; each room has a different wall type, dampness and
 lighting as a quality and exits to certain directions.
 Treasure is either in the room or not.
"""

class Room():

    def __init__(self, room_pos_x, room_pos_y, room_exits, room_has_treasure):
        self.room_pos_x = room_pos_x
        self.room_pos_y = room_pos_y
        self.room_exits = room_exits # list of integers, n-e-s-w order, 0 or 1
        self.room_has_treasure = room_has_treasure

    def get_room_position(self):
        return self.room_pos_x, self.room_pos_y

    def get_room_exit_directions(self):
        return self.room_exits

    def get_room_has_treasure(self):
        return self.room_has_treasure

class MoveAround():

    def __init__(self):
        self.player_pos_x = 0
        self.player_pos_y = 0

        # Start MAIN LOOP
        self.startgame()


    def generate_room(self):
        self.room_exit_list = []
        print("You are in position %d, %d on the map.\n" % (self.player_pos_x, self.player_pos_y))

        # Look around in room and identify exits.
        if maze_map[self.player_pos_y][self.player_pos_x].get_room_exit_directions()[0] == 1:
            self.room_exit_list += ["north"]
        if maze_map[self.player_pos_y][self.player_pos_x].get_room_exit_directions()[1] == 1:
            self.room_exit_list += ["east"]
        if maze_map[self.player_pos_y][self.player_pos_x].get_room_exit_directions()[2] == 1:
            self.room_exit_list += ["south"]
        if maze_map[self.player_pos_y][self.player_pos_x].get_room_exit_directions()[3] == 1:
            self.room_exit_list += ["west"]

        print("Room has doors in the following directions:" + str(self.room_exit_list) + ".")

        # Does room have treasure?
        if maze_map[self.player_pos_y][self.player_pos_x].get_room_has_treasure() == 1:
            print("BINGO! The treasure is in this room!\n")
        else:
            print("The treasure is not in this room.\n")


    def input_command(self):
        self.player_move_x = 0
        self.player_move_y = 0
        print("Enter your command!\n")
        command = input()
        valid_commands = ["north", "east", "south", "west", "q"]
        if command in valid_commands and command not in self.room_exit_list:
            print("There is no door that way!")
        elif command == "north":
            self.player_move_y = 1
        elif command == "east":
            self.player_move_x = 1
        elif command == "south":
            self.player_move_y = -1
        elif command == "west":
            self.player_move_x = -1
        elif command == "q":
            self.quitgame()
        else:
            print("Please enter direction 'north', 'east', 'south', 'west'\n to move in direction or letter 'q' to quit!")
        return self.player_move_x, self.player_move_y

    def move_player(self):
        # INSERT: check if there is door

        # Move player
        self.player_pos_x += self.player_move_x
        self.player_pos_y += self.player_move_y

    # Game start, end and loop
    def startgame(self):
        self.is_running = 1
        print("The game is starting!\n")
        self.game_loop()

    def quitgame(self):
        self.is_running = 0

    def game_loop(self):
        while self.is_running == 1:
            self.generate_room()
            print("**************\n")
            self.input_command()
            self.move_player()
        print("\nThe game has ended!\n" + "Thank you for playing! Bye!")

# Kick off the game

room_1 = Room(0, 0, [0, 1, 0, 0], 0)
room_2 = Room(1, 0, [0, 1, 0, 1], 0)
room_3 = Room(2, 0, [0, 0, 0, 1], 1)

# My classes are put within a multi-dimensional array (list):
# Each row is an y, each
maze_map = [room_1, room_2, room_3], []

walkaround = MoveAround()
