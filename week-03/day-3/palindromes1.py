# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 16:02:24 2016

@author: gergov
"""

class MakePalindrome():
    
    reversedstring = []
    outputstring = []
    
    def __init__(self, inputstring):
        self.inputstring = list(inputstring)
        
    def makeItPalindrome(self):
        for i in range(len(self.inputstring)-1, -1, -1):
            self.reversedstring += self.inputstring[i]
        self.outputstring = self.inputstring + self.reversedstring
        self.outputstring
        return self.outputstring
        
PPAP = MakePalindrome("apple")
print(PPAP.makeItPalindrome())
