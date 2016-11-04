# create a pirate class
# it should have 2 methods
# drink_rum()
# hows_goin_mate()
# if the drink_rum was called at least 5 times:
# hows_goin_mate should return "Arrrr!"
# "Nothin'" otherwise

# Added attributes name and rounds needed to get drunk and option to drink more shots in a round.

class Pirate():    
    
    def __init__(self, name, limit):
        self.rounds = 0
        self.name = name
        self.getdrunk = limit
    
    def drink_rum(self, shots):
        self.rounds += shots

    def hows_it_goin_mate(self):
        if self.rounds >= self.getdrunk:
            print("Arrrr!")
        else:
            print("Nothin'")


pirate1 = Pirate("Roger", 7)
pirate2 = Pirate("Davies", 3)

pirate1.drink_rum(3)
pirate1.hows_it_goin_mate()
