names = ['Zakarias', 'Hans', 'Otto', 'Ole', 'Peter', 'Robert', 'James']
# create a function that returns the shortest string
# from a list

"""
WRONG
def sname(val):
    target = "Zebra"
    
    for n in val: # Pick each element
        for i in range(0, len(val)): # Pick element to compare to element including itself
            if len(n) < len(val[i]): # If element is shorter than other, 
                target = n # this is one we look for (short)
            else: # If element is not shorter than other,
                target = val[i] # we are looking for the other one.
                
    return target

print(sname(names))
print("I'm done.")
"""

def sname(val):
    shorter = "Zebra"
    
    for n in val: # Pick each element
        for i in range(0, len(val)): # Pick element to compare to element including itself
            if n == val[i]:
                break # don't compare itself with itself
            elif len(n) < len(val[i]): # If element is shorter than other, 
                shorter = n # we are looking for n.
            else:
               shorter = val[i] # If not, we are looking for the other one.
            
            final = shorter                
            print("Examined item:",n,"; Compared to:",val[i],"; Shorter:",shorter)
                
    return final

print("Shortest name is:",sname(names))
print("I'm done.")
