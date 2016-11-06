# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has

class drawme:
    
    def __init__(self, lines):
        self.lines = lines
        
    def drawit(self):
        for i in range(1, self.lines +1):
            print(i * "*")
            
triangle = drawme(5)
triangle.drawit()
