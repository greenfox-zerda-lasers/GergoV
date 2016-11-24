import csv

class AreaMap:

    def __init__(self):
        self.area_floorplan = []

        with open('./mapdata.csv', 'r', newline='') as f:
            f_reader=csv.reader(f, delimiter=',')
            for line in f_reader:
                self.area_floorplan.append(line)

    def get_area_floorplan(self):
        return self.area_floorplan

    def get_area_dimensions(self):
        self.area_dimensions = [len(self.area_floorplan), len(self.area_floorplan[0])]
        # NOTE to self: Number of rows, number of columns
        return self.area_dimensions

class Hero:

    def __init__(self):
        self.hero_position = [0, 0]

    def get_hero_position(self):
        return self.hero_position

    def set_hero_position(self, alteration):
        self.hero_position[0] += alteration[0]
        self.hero_position[1] += alteration[1]
