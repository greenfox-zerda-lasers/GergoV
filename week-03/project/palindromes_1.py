# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:18:28 2016

@author: gergov

Create a function that takes a string and creates a palindrome from it. It should work like this:

    output = create_palindrome('pear')

    print(output) # it prints: pearraep

"""

def create_palindrome(text):
    inverted = ''
    for i in range(len(a), 0, -1):
        inverted += text[i-1]
    return text + inverted

output = create_palindrome('pear')

print(output) # it prints: pearraep
