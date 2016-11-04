# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Stack():
    
    def __init__(self):
        self.storage = [] # This is the list of elements.
    
    def push(self, item):
        self.storage += [item]
        print("Element",[item],"added")
        return self.storage
            
    def size(self):
        self.storage_size = len(self.storage)
        print("Stack has",self.storage_size,"elements")
        return self.storage_size
        
    def pop(self):
        self.lastelement = self.storage[len(self.storage)-1]
        print("Element", self.lastelement, "is to be deleted.")
        del self.storage[len(self.storage)-1]
        return self.storage
        
myStack = Stack()
print("Stack created")
myStack.push("Apple")
myStack.push("Apple")
myStack.push("Pen")
myStack.push("Apple")
myStack.push("Pineapple")
