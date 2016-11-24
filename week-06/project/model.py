import csv

class AreaMap:

    def __init__(self):
        self.area_floorplan = []
        self.valid_character_positions = []

        with open('./mapdata.csv', 'r', newline='') as f:
            f_reader=csv.reader(f, delimiter=',')
            for line in f_reader:
                self.area_floorplan.append(line)

        self.area_dimensions = [len(self.area_floorplan), len(self.area_floorplan[0])]
        # NOTE: rows, columns (y, x!)

        self.valid_character_positions = []

        for row in range(self.area_dimensions[0]):
            for column in range(self.area_dimensions[1]):
                if self.area_floorplan[row][column] == 0:
                    self.valid_character_positions.append([column, row])


    def get_area_floorplan(self):
        return self.area_floorplan

    def get_area_dimensions(self):
        return self.area_dimensions

    def get_valid_character_positions(self):
        return self.valid_character_positions

class Hero:

    def __init__(self):
        self.hero_position = [0, 0]

    def get_hero_position(self):
        return self.hero_position

    def set_hero_position(self, alteration):
        self.hero_position[0] += alteration[0]
        self.hero_position[1] += alteration[1]

class Boss:

    def __init__(self, position, hp, dp, sp):
        self.position = position
        self.hp = hp
        self.dp = dp
        self.sp = sp

class Skeleton:

    def __init__(self, position, hp, dp, sp, has_key):
        self.position = position
        self.hp = hp
        self.dp = dp
        self.sp = sp
        self.has_key = has_key
