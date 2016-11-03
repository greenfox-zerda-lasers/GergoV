numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function

def mysum_range(value):
    summa = value[0]    
    
    print("Ezeket adom ossze:", value)
    
    for i in range(1, len(value)):
        pos = i - 1
        tobeadded = value[pos + 1]
        print(i,".lepes: Itt allok:",pos,". elem; erteke:", value[pos])
        print("Eddig ennyi az osszeg:", summa)
        summa = summa + tobeadded
        print("Ezt adom hozza:", tobeadded, ", igy a reszosszeg:",summa)
        print("")
    return summa

    
print("A vegeredmeny:",mysum_range(numbers))