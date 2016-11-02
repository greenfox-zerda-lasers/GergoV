ah = ['kuty', 'macsk', 'cic']
# add to all elements an 'a' on the end

n = len(ah)

print(ah)

while n > 0:
    n = n - 1
    ah[n] = ah[n] + "a"
    
print ("Ready:", ah)