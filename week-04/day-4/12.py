# 12. write a recursive function that can add numbers in
# [1, 2, [3, 4], 1, [1, [2, 4]]]

def add_list(a):
    if a[0] == []:
        return 0
    elif isinstance(a, list):
        return add_list(a)
    else:
        return a[0] + add_list(a[1:])

a = [1, 1, 1, 2, 2]
b = [1, 2, [3, 4], 1, [1, [2, 4]]]
out = add_list(b)
print(out)
