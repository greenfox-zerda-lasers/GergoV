k = 1521
# tell if k is dividable by 3 or 5

basefive = k % 5
basethree = k % 3

if basefive > 0:
    dvblefive = False
if basefive == 0:
    dvblefive = True
if basethree > 0:
    dvblethree = False
if basethree == 0:
    dvblethree = True
    
print(k, "is dividable by")
print("Five: ", dvblefive)
print("Three: ", dvblethree)  

# The better method:

print("Dividable by 5?", k % 5 == 0 )
print("Dividable by 3?", k % 3 == 0 )