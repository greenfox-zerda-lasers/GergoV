# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 13:58:01 2016

@author: gergov
"""

def sentence(*words):
    word_list = list(words)
    lowercased = []
    
    for i in range(0, len(word_list)):
        lowercased.append(word_list[i].uppper())
      
        print(lowercased)
               
  
    return sentence

sentence("this","is","a","sentence", "lol")