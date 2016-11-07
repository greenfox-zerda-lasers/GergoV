# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:21:15 2016

@author: gergov
"""

# 6. Create a method that gets a list of integers and gives back a string which characters are created from the numbers used as character codes
def string(*char_codes):
    letterlist = []
    for i in char_codes:
        letterlist += chr(i)
    output = "".join(letterlist)
    print(output)

string(97, 101, 111, 113)