numbers = [7, 5, 8, -1, 2]

# numbers = [5, 1, 5]

# Write a function that returns the minimal element
# in a list (your own min function)

# *** I Also wanted to check if there is no smallest, when all numbers are equal. Work in progress.. ***

val = numbers
noihavetobesmallerthan = len(val) -1
howmanybiggerthanme = {}

for i in val: # I pick each element one by one.
    howmanybiggerthanme[i] = 0; # I set counter value of index i 0.
    for pos in range(0, len(val)): # I put each element's position number in pos.
        other = val[pos] # I pick 'other' element in position pos.
        if i < other: # If i is smaller than 'other' element
            print(i,"is smaller than", other,"which is in position",pos)
            # 
            howmanybiggerthanme[i] = howmanybiggerthanme[i] + 1 
for i in val: # I examine them again, so pick each element...
    if howmanybiggerthanme[i] == noihavetobesmallerthan: # if I am smaller then all-1
        smallestnumber = i # I am the smallest number
        biggerthansmallestnumber = howmanybiggerthanme[i] # No. of elements bigger than me
        print("")
        print("I found out that")
        print(smallestnumber,"is the smallest of these elements:",val,",")
        print("as there are",len(val),"elements in the list")       
        print("and",biggerthansmallestnumber,"elements are bigger than it.")
        print("")
