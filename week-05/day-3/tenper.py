# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 10:22:31 2016

@author: gergov
"""

# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def tenper(numin):
    try:
        # numin = input("Please give me a number! ")
        numout = 10 / int(numin)
        print(numout)
    except ValueError:
        print("Please input integer only!") 
    except ZeroDivisionError:
        #print("fail")
        return 'fail'