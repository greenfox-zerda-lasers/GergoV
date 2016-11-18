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

import texts, argparse, csv

class Control():

    def __init__(self):
        self.parseInput()

    def parseInput(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-l', '--list', action='store_true', help='List todo items')
        parser.add_argument('-a', '--add', action='store_true', help='Add item')
        parser.add_argument('-r', '--remove', action='store_true', help='Remove item')
        parser.add_argument('-c', '--check', action='store_true', help='Mark item checked')
        args = parser.parse_args()
        if args.list:
            self.list_todo()
        elif args.add:
            print('Add item')
        elif args.remove:
            print('Remove item')
        elif args.check:
            print('Check item')
        else:
            self.print_welcome()

    # Main functions

    def list_todo(self):
        f = open('data.csv', newline='')
        reader = csv.reader(f)
        rownum = 0
        for row in reader:
            rownum += 1
            print(rownum, '-', ''.join(row))

    def add_todo(self):
        f = open('data.csv', 'wb')
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(f)


    def check_todo(self):
        # write model
        pass

    def remove_todo(self):
        # write model
        pass


    def check_storage(self):
        try:
            data = open('data.py', 'r')
            data.close()
        except FileNotFoundError:
            open('data.py', 'wb')


    def print_welcome(self):
        print(texts.welcome)


# Init program
todolist = Control()
