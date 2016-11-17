# Write a Person class that have a name and a birth_date property
# It should raise an error of the birthdate is less than 0 or more than 2016

class Person():
        
        def __init__(self, name, birthdate):
            self.name = name
            self.birthdate = birthdate
            if self.birthdate > 2016 or self.birthdate < 0:
                raise ValueError("Invalid birthdate, yo")
                
        def get_name(self):
            return self.name
            
        def get_birthdate(self):
            return self.birthdate
                
