# Write a program that prints the numbers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

n = 0

while n < 100:
    n += 1
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elseif n % 3 == 0