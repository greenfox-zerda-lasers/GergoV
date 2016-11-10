# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).

def ears(n):
    if n == 1:
        return 2 # base value: no. or ears / bunny
    else:
        return ears(n - 1) + 2

print(ears(5))
