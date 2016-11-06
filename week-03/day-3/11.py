# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has


class drawmediamond:
    
    indentsinrow = 1
    
    def __init__(self, lines):
        self.lines = lines
        
    def drawit(self):
        for i in range(0, self.lines): 
            if i <= self.lines // 2: # To center line, if odd no. of lines
                aster = i * 2 + 1 # *2 + 1 to make it odd; 0 becomes 1
            if i > self.lines // 2:
                # n is: steps taken from x // 2 to last step
                n = i - (self.lines - i)
                aster = (i * 2) - (n * 2) - 1
            indents = (self.lines * 2 - aster) // 2 - 3 # The remaining space between x(max) not filled, /2 because indent left; donno why too much
            print(indents * " " + aster * "*")

"""
1st version: calculation + pirmitive steps

class drawmediamond:
    
    indentsinrow = 1
    
    def __init__(self, lines):
        self.lines = lines
        
    def drawit(self):
            
        for i in range(1, self.lines + 1):   
            if i <= (self.lines // 2) + 1:
                self.starsinrow = i + (i - 1)
                self.indentsinrow = self.lines - i - 1 # Until here I can calculate
            else: # Here comes primitive: decreasing/increasing in steps
                self.starsinrow -= 2
                self.indentsinrow += 1
                
                
            print(self.indentsinrow * " " + self.starsinrow * "*")
            
"""
          
primitivediamond = drawmediamond(11)
primitivediamond.drawit()