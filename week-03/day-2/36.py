numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list


def reorder(value):
    print("Number of elements:", len(value))
    
    neworder = []
    
    for i in range(0, len(value)):
        print(i)
        oldpos = len(value) - i - 1
        #neworder.append(value[oldpos])
        neworder = neworder + [value[oldpos]] # without append: add a list to list
        print("Old position to fetch from:", oldpos)
    
    return neworder
    
print(reorder(numbers))
