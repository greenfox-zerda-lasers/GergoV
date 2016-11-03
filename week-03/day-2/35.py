# create a function that returns it's input factorial

def fact_n(value):
    factorial = value
    print("Feldolgozando ertek:", factorial)
    for n in range(value - 1, 1, -1):
        print("Ez az akutalis ertek:", n)
        factorial = factorial * n
    return factorial 

print(fact_n(5))