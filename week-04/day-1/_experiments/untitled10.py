# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 14:07:35 2016

@author: gergov
"""

# 5. Create a method that gets a string and gives back the character codes in a list
def char_codes(string):
    string_letter_list = []
    for i in string:
        string_letter_list.append(ord(i))
    return string_letter_list
    
print(char_codes("Kawungabogagabogata"))

# ord, chr

