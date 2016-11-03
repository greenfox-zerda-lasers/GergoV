numbers = [3, 4, 5, 6, 7]
# write a function that filters the odd numbers
# from a list and returns a new list consisting
# only the evens

def filterodd(value):

    newlist = []
    
    for n in value:
        if n % 2 == 0:
            continue
        else:
            newlist.append(n)
    
    return newlist
    
print(filterodd(numbers))     