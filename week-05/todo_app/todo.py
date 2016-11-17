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


# Define

class Item():
    pass


def handle_input():
    # generic idea: get parameter, call function for parameter based on a dict.
    command = input("\nWhat do you want to do today?\n")
    if command in commlist:
        commlist['l']()        
    else:
        print(texts.input_error_notarg)
        handle_input()

    
def list_todo():
    pass
    
def add_todo():
    pass
    
def check_todo():
    pass

def remove_todo():
    pass

commlist = {'l':list_todo, 'a':add_todo, 'c':check_todo, 'r':remove_todo}
    

def check_storage():
    try:
        data = open('data.py', 'r')
        data.close()
    except FileNotFoundError:
        open('data.py', 'wb')    


# Execute
print(texts.intro['main'])
check_storage()
handle_input()

a = [Item()]
a.append(Item())
b = Item()
a.append(b)
print(a)


