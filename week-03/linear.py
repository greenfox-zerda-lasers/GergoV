# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 21:38:15 2016

@author: gergov
"""

x = 7

# half-diamond

for i in range(1, (x // 2) + 1):  
    stars = i
    
    print(stars * "*")
    
for i in range((x // 2) + 2, x):  
    stars = x - i

    print(stars * "*")
    
# full diamond
    
for i in range(1, (x // 2) + 1):  
    stars = i
    
    print(stars * "*")
    
for i in range((x // 2) + 2, x):  
    stars = x - i

    print(stars * "*")
