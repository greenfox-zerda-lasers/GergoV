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
            
        for i in range(1, self.lines + 1):   
            if i <= (self.lines // 2) + 1:
                self.starsinrow = i + (i - 1)
                self.indentsinrow = self.lines - i - 1 # Until here I can calculate
            else: # Here comes primitive: decreasing/increasing in steps
                self.starsinrow -= 2
                self.indentsinrow += 1
                
                
            print(self.indentsinrow * " " + self.starsinrow * "*")
            
          
          
primitivediamond = drawmediamond(9)
primitivediamond.drawit()