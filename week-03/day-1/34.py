ag = [3, 4, 5, 6, 7]
# please double all the elements of the list

'''
print("Eredeti lista:",ag)
for f in ag:
    print("Eredeti:",f)
    ag[f] = ag[f] * 2
    print("Dupla:", ag[f])
print("Kesz lista:",ag)
'''


# so it does not work now

print("A lista:", ag)

for n in ag:
    print("Eredeti:",n)
    n = n * 2
    print("Duplazott:", n)

print("Kesz:", ag)