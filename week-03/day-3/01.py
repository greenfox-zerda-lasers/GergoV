# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's area

class Circle:
    
    pi = 22 / 7

    def __init__(self, r):
        self.radius = r
    
        
    def get_circumference(self):
        cfc = self.radius * 2 * self.pi
        return cfc
        
    def get_area(self):
        area = self.radius ** 2 * self.pi
        return area
                
mycircle = Circle(23)
print(mycircle.get_circumference())
print(mycircle.get_area())       