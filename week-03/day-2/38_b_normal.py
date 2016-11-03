# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 17:26:37 2016

@author: gergov
"""

numbers = [7, 5, 8, -1, 2, -5]

# numbers = [5, 1, 5]

# Write a function that returns the minimal element
# in a list (your own min function)

def fsmallest(val):
    for i in val:
        smallest = val[0]
        for j in val:
            if smallest > j:
                smallest = j
    return smallest

print(fsmallest(numbers))
        