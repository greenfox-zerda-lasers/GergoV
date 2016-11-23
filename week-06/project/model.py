import csv

class GameData:

    def __init__(self):
        self.get_area_floorplan()

    def get_area_floorplan(self):
        self.area_floorplan = []

        with open('./mapdata.csv', 'r', newline='') as f:
            f_reader=csv.reader(f, delimiter=',')
            for line in f_reader:
                self.area_floorplan.append(line) # becomes list of lists, each line is a list

        return self.area_floorplan

class Hero:

    def __init__(self):
        self.hero_position = [0, 0]

    def get_hero_position(self):
        return self.hero_position
