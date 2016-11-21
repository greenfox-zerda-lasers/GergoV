
import texts, sys, csv

class Control():

    def __init__(self):
        self.parseInput()

    def parseInput(self):
        argcommands = {"-l": self.list_todo, "-a": self.add_todo, "-c": self.check_todo, "-r": self.remove_todo}
        if len(sys.argv) < 2:
            self.print_welcome()
        else:
            argcommands[sys.argv[1]]()

    # Main functions

    def print_welcome(self):
        print(texts.welcome)

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

    def add_todo(self):
        if len(sys.argv) < 3:
            print(texts.input_error_add_notodo)
        else:
            item = sys.argv[2]
            f = open('data.csv', 'a')
            writer = csv.writer(f, delimiter=',');
            writer.writerow(item)
            f.close()

    def check_todo(self):
        # write model
        pass

    def remove_todo(self):
        csv_cache = []
        f = open('data.csv', 'r', newline='')
        fw = open('data.csv', 'w', newline='')
        reader = csv.reader(f, delimiter=',')
        writer = csv.writer(fw, delimiter=',')
        for row in reader:
            csv_cache += row
        for i in len(range(csv_cache)):
            if i == csv.argv[2]:
                csv_cache[i].pop()
        for i in csv_cache:
            writer.writerow(i)
        f.close()
        print('Task' + {} + 'deleted.'.format(sys.argv[2]))


    def check_storage(self):
        try:
            data = open('data.py', 'r')
            data.close()
        except FileNotFoundError:
            open('data.py', 'wb')


# Init program
todolist = Control()
