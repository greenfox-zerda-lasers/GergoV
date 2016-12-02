# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:18:28 2016

@author: gergov

Create a function that searches for all the palindromes in a string that are at least than 3 characters, and returns a list with the found palindromes. Example:

    output = search_palindromes('dog goat dad duck doodle never')
    print(output) # it prints: ['og go', ' dad ', 'd d', 'dood', 'eve']
"""

def search_palindromes(text):
    palindrome_list =[]
    if len(text) >= 3:
        for i in range(0, len(text)-1):
            specimen_list = []
            specimen = ''
            for j in range(i, len(text)):
                specimen += text[j]
                specimen_list.append(specimen)
            for k in specimen_list:
                reversed_specimen = ''
                for l in range(len(k), 0, -1):
                    reversed_specimen += k[l-1]
                if k == reversed_specimen and len(k) >= 3:
                    palindrome_list.append(k)
                
        return palindrome_list
    
    else:
        print('Input too short.')


output = search_palindromes('dog goat dad duck doodle never')
print(output) # it prints: ['og go', ' dad ', 'd d', 'dood', 'eve']
