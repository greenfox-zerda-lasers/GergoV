'''
Features:
    - list todo
    - add todo
    - complete todo
    - remove todo

Functions:
    - Handling input
        - a., normal
        - b., from command line
    -Print output
    - Todo item
        - Description
        - Status (not done/done)
    -
'''

import texts #,data

class Control():

    def __init__(self):
        self.Model = Model()
        self.View = View()
        self.commands = {'l': self.list_todo, 'a': self.add_todo, 'c': self.check_todo, 'r': self.remove_todo}

        self.handle_input()

    def handle_input(self):
        command = input("Yes master?\n")
        if command in self.commands:
            self.commands['l']()
        else:
            print(texts.input_error_notarg)
            self.handle_input()

    # Main functions

    def list_todo(self):
        # read from file - model
        # print list
        pass

    def add_todo(self):
        # write model
        pass

    def check_todo(self):
        # write model
        pass

    def remove_todo(self):
        # write model
        pass


class Model():

    def __init__(self):
        self.tasklist = [] # Function tests

    def check_storage(self):
        try:
            data = open('data.py', 'r')
            data.close()
        except FileNotFoundError:
            open('data.py', 'wb')

class View():

    def __init__(self):
        pass




# Execute program
# todolist = Control()


print(texts.input_error_notarg)
