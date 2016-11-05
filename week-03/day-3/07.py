# create a function that takes a list and returns a new list with all the elements doubled

class DoubleEm:
    
    items = []
    
    def __init__(self, *items):
        self.items = items
    
    def show(self):
        print("This is your list:" + str(self.items))
        
    def double(self):
        for i in self.items:
            doubleitem = i * 2
            
            
        

skunk = DoubleEm(4, 5, 6, 7, 8)
skunk.show()