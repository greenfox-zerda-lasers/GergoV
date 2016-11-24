import csv

class Try:

    def __init__(self):
        self.area_floorplan = []

        with open('./mapdata.csv', 'r', newline='') as f:
            f_reader=csv.reader(f, delimiter=',')
            for line in f_reader:
                self.area_floorplan.append(line)

        self.area_dimensions = [len(self.area_floorplan), len(self.area_floorplan[0])]
        # NOTE: rows, columns (y, x!)

        self.valid_character_positions = []

        for row in range(self.area_dimensions[0]):
            for column in range(self.area_dimensions[1]):
                if int(self.area_floorplan[row][column]) == 0:
                    self.valid_character_positions += [[column, row]]

        print(self.valid_character_positions)



runthis = Try()
