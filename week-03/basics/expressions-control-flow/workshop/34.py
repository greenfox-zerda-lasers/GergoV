ag = [3, 4, 5, 6, 7]
# please double all the elements of the list

n = len(ag)
print("Ag has", n,"elements.")
print(ag)

while n > 0:

# n becomes pos here!!!
    n -=1
    ag[n] = ag[n] * 2

print("After *2 elements:",ag)