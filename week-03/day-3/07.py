# create a function that takes a list and returns a new list with all the elements doubled

class DoubleEm:    
    
    def __init__(self, *items): # make it accept ? no of arguments with *
        self.items = items
        
    
    def show(self):
        print("This is your list:" + str(self.items))
        
    def double(self):
        self.newlist = [] #need to define
        for i in self.items:
            newitem = i*2
            print(i, "->",newitem) #just to see clearly
            self.newlist = self.newlist + [newitem]
        print(self.newlist)


mylist = DoubleEm(4, 5, 6, 7, 8) # list elements as a parameter
mylist.show()
mylist.double()
