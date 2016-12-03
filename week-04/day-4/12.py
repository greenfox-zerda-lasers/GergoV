# 12. write a recursive function that can add numbers in
# [1, 2, [3, 4], 1, [1, [2, 4]]]


def add_list(foo):
    if len(foo) == 0:
        return 0
    elif type(foo) == list:
        return add_list(foo[0]) + add_list(foo[1:])
    else:
        return foo[0] + add_list(foo[1:])

print(add_list([1, 2, [3, 4], 1, [1, [2, 4]]]))
