# -*- coding: utf-8 -*-
"""
Bucky's Intro to classes

Created on Fri Nov  4 11:06:25 2016

@author: gergov
"""

class Enemy:
    life = 3
    
    def attack(self):
        print("Ouch! I'm hit!")
        self.life -= 1
        
    def checklife(self):
        if self.life <= 0:
            print("I am dead!")
        else:
            print(str(self.life) + " life left")
            
enemy_1 = Enemy()
enemy_2 = Enemy()

enemy_1.attack()

enemy_1.checklife()
enemy_2.checklife()