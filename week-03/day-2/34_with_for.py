numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function

def mysum(value):
    print("Ezeket adom ossze:", value)
    summa = 0
    for n in value:
        summa = summa + n
        print("Elem:", n, "Reszosszeg:", summa)
    return summa
    
print(mysum(numbers))
    
