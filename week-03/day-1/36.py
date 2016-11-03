ah = [3, 4, 5, 6, 7]
# print the sum of all numbers in ah

n = len(ah)
sum_ah = 0

print("Ezt add össze:", ah)

while n > 0:
    n = n - 1
    # Ez a pontos pozícióm: n darabszám, n-1: pozíció.
    print(n + 1,". poziíció, itt szereplő érték:", ah[n])
    print("Művelet:", sum_ah,"+",ah[n])
    sum_ah = sum_ah + ah[n]
    print("Végeredmény:", sum_ah)
  
print("*********")
print("Amikor kész, a tejes végeredmény:",sum_ah)    