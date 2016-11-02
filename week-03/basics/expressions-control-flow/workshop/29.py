ab = 123
credits = 100
is_bonus = False

# if credits are at least 50,
# and is_bonus is False decrement ab by 2
if credits >= 50 and is_bonus == False:
    ab = ab - 2

# if credits are smaller than 50,
# and is_bonus is False decrement ab by 1
if credits < 50 and is_bonus == False:
    ab = ab -1

# if is_bonus is True ab should remain the same

print("Primitive:",ab)

if is_bonus == False:
    pass
elif credits >= 50:
    ab = ab - 2
elif credits <= 50:
    ab = ab - 1

print("Compact:",ab)