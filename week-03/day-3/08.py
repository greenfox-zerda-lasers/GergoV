# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person:
          
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
     
    def greet(self):
        print("Hi, I'm the Parent, my name is " + self.firstname + " " + self.lastname + ".")

        
class Student(Person):
    
    grades = []
    gradesum = 0
    average = 0
    
    def __init__(self, firstname):
        self.firstname = firstname
        
    def setparent(self, obj):
        self.parent = obj
        self.student_lastname = self.parent.lastname
        
    def addgrade(self, newgrade):
        self.grades += [newgrade]
        print("Grade " + str(newgrade) + " added.")
        print("These are my grades:" + str(self.grades))

    def salute(self):
        print("Hi, I'm the Student, my name is " + self.firstname + " " + self.student_lastname + ".")

        # Don't divide by 0.
        for i in self.grades:
            self.gradesum += i
        
        if self.gradesum == 0:
            print("I have no grades yet.")
        else:
            self.average = self.gradesum / len(self.grades)
            print("The average of my grades is:" + str(self.average))
        

     
Homer = Person("Homer","Simpson")
Bart = Student("Bart")
Bart.setparent(Homer)

Homer.greet()
Bart.salute()

Bart.addgrade(5)
Bart.addgrade(4)

Bart.salute()
