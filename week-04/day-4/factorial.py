def factorial(number):
    product = 1
    for i in range(number):
        product += product * i
    return product

print(factorial(5))
