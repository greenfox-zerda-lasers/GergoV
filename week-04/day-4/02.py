# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def rec_addem(n):
    if n <= 1: # base case: reached 1
        return 1
    else:
        return n + rec_addem(n - 1)

print(rec_addem(3))
