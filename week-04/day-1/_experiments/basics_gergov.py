# -*- coding: utf-8 -*-
"""
Work in progress

Created on Mon Nov  7 10:51:36 2016

@author: gergov
"""

def sentence(*words):
    word_list = list(words)
    word_list[0] = str.title(word_list[0])
    output = ' '.join(word_list)
    output += '.'
    return output

print(sentence("this","is","a","sentence"))