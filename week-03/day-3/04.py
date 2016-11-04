# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class myClass():
    
    def __init__(self):
        self.average = 0
        self.gradesum = 0
        self.gradelist = []
        
    def add_grade(self, grade):
        # self.grade = grade
        if grade > 5 or grade < 1:
            print("Pleade enter a valid grade (1-5)!")
        else:
            self.gradelist.append(grade)
            print("Grade " + str(grade) + " added")
            print("Grades are:" + str(self.gradelist))
          
    def get_average(self):
        for i in self.gradelist:
            self.gradesum += i
        self.average = self.gradesum / len(self.gradelist)
        return self.average
          
HatodikB = myClass()

HatodikB.add_grade(4)
HatodikB.add_grade(4)
HatodikB.add_grade(5)

print(HatodikB.get_average())