# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

"""
def recurdown(n):
    print(n)
    n = n - 1
    if n >= 0:
        recurdown(n)
    return n
"""
def recurdown(n):
    print(n)
    if n == 1: # base case: Reached 1
        return n
    else:
        return recurdown(n - 1)


recurdown(10)
