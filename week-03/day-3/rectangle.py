# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 10:44:48 2016

@author: gergov
"""

rectangle1 = {"a": 40, "b": 50}
rectangle2 = {"a": 20, "b": 30}

class Rectangle():
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
        print('Recangle\'s')
        print('a side length =' + str(self.a))
        print('b side length =' + str(self.b))
        print('Ready to calculate')


    def get_circumference(self):
        circumference = ( self.a * 2 ) + ( self.b * 2 )
        return circumference

    def get_area(self):
        area = self.a * self.b
        return area
        

# Defininig object

myrect = Rectangle(10, 20)
print('')
print(myrect.get_circumference())
print(myrect.get_area())
