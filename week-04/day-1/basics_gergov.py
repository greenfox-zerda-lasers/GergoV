# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 10:51:36 2016

@author: gergov
"""

def readline(file_name, number):
    f = open(file_name)
    result = f.readlines()[number-1].rstrip()
    f.close()
    return result

print(readline('texts/zen_of_python.txt', 4))