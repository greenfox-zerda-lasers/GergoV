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
        parser.add_argument('-a', '--add', action='store_true', type=str, help='Add item')
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
        f = open('data.csv', 'r', newline='')
        reader = csv.reader(f, delimiter=',')

        f.seek(0)
        first_char = f.read(1)
        if not first_char:
            print(texts.list_empty)
        else:
            f.seek(0) # Reset reader to char 0
            for row in reader:
                rowcontent = ''.join(row)
                print(reader.line_num, '-', rowcontent)
        f.close()

    def add_todo(self, item):
        f = open('data.csv', 'a')
        f.write(item)
        f.close()


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
