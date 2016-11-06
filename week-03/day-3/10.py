# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has

class drawmetree:
    
    def __init__(self, lines):
        self.lines = lines
        
    def drawit(self):
        for i in range(1, self.lines + 1):
            self.starsinrow = i + (i - 1) 
            self.indentsinrow = self.lines - (i - 1)
            # print(i, ":", self.indentsinrow, self.starsinrow)
            print(self.indentsinrow * " " + self.starsinrow * "*")
            
          
          
triangle = drawmetree(5)
triangle.drawit()
