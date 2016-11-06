# create a function that takes a list and returns a new list that is reversed

class ReverseList():
    
    def __init__(self, *items):
        self.items = items
        
        
    def reverseEm(self):
        self.newlist = []
        for i in range(len(self.items), 0, -1): #len =6, from 6 to 0 by -1
            newitem = self.items[i-1]
            self.newlist = self.newlist + [newitem]
        return self.newlist
            

myList = ReverseList(4, 5, 6, 7, 8, 9)
myList.reverseEm()
print(myList.items)
print(myList.newlist)           