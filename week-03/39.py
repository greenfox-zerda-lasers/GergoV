names = ['Zakarias', 'Hans', 'Otto', 'Ole', 'Peter', 'Robert', 'James']
# create a function that returns the shortest string
# from a list

def fshortest(val):
    for i in val:
        obj = val[0]
        for j in val:
            if len(obj) > len(j):
                obj = j
    return obj
    
print(fshortest(names))