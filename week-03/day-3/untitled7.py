# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:44:48 2016

@author: gergov
"""

class Rectangle():
    a = 0
    b = 0

    def __init__(self, a, b):
        print('YAY', a)
        self.a = 0
        self.b = 0

    def get_circumference(self):
        return self.a * 2 + self.b * 2

myrect = Rectangle(10, 20)
print(myrect.get_circumference)



"""
This is green!

"""
