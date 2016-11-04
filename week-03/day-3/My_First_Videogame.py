
# -*- coding: utf-8 -*-
"""
More on classes and objects

Created on Fri Nov  4 11:06:25 2016

@author: gergov
"""

class Enemy:
    
    characteristic = "Evil" # All enemies are evil! Class variable, a többiek instance varok.
    
    # Init: TKP. egy hívás nélkül, magától lefutó metódus.
    def __init__(self, name, energy):
        self.energy = energy
        self.name = name
        print("An enemy called",self.name,"appeared!")
        print("It has",self.energy,"life!")
    
    def attack(self):
        print(self.name + ": Ouch! I'm hit!")
        self.energy -= 1
        
    def checklife(self):
        if self.energy <= 0:
            print(self.name,": I am dead!")
        else:
            print(self.name,"has",str(self.energy) + " life left.")
            
enemy_1 = Enemy("Jason", 99)
enemy_2 = Enemy("Minion", 15)
print("")

enemy_1.attack()
enemy_1.checklife()

