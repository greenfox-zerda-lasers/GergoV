
# 3. Given a non-negative int n,
# return the sum of its digits recursively (no loops).
# Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6),
# while divide (//) by 10
removes the rightmost digit (126 // 10 is 12).


def add_dig(n):
    if n // 10 == 0:
        return n
    else:
        return add_dig(n // 10) + n % 10

print(add_dig(123))
