# Create an elevator controller class
# It should take an user input by listening to user input
# List of commands:
#
#  - Move elevator up
#  - Move elevator down
#  - Add people
#  - Remove people
#
#  Features to implement:
#   - Always draw the state of the elevator as depicted in "art.txt"
#   - [ x ] is the elevator. X means it has at least 1 person inside
#   - Moving floors should take time
#   - don't move beyond limits
#
# Create the class with MVC pattern in mind. It should get and store data in the model object
# and it should pass the data to the view objects

import model_elevator, view_elevator, os

class Controller():

    def __init__(self):
        self.model = model_elevator.Elevator()
        self.view = view_elevator.Display()

        # Init mainloop
        self.should_run = True
        self.mainLoop()

    def mainLoop(self):
        while self.should_run == True:
            self.drawScreen()
            self.handleInput()
            self.mainLoop()

    def handleInput(self):
        command = input("What do you want to do?\n")
        self.commandlist = { "u": self.elevatorUp, "d": self.elevatorDown, "i": self.addPassengers, "o": self.rmPassengers, "q": self.quitGame }
        if command in self.commandlist:
            self.commandlist[command]()
        else:
            print("Invalid command.")
            self.handleInput()

    def elevatorUp(self):
        self.model.setPosition(1)
        print("Elevator Up")

    def elevatorDown(self):
        self.model.setPosition(-1)
        print("Elevator Down")

    def addPassengers(self):
        self.model.addPeople(1)
        print("P+")

    def rmPassengers(self):
        self.model.addPeople(-1)
        print("PI")

    def quitGame(self):
        self.should_run = False
        print("You chose to quit. Goodbye!")

    def drawScreen(self):
        os.system('clear')
        self.view.displayElevator(self.model.getFloors(), self.model.getPosition(), self.model.getPassengers())
        self.view.displayConsole()


# Init program

loveinanelevator = Controller()
