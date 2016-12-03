# 12. write a recursive function that can add numbers in
# [1, 2, [3, 4], 1, [1, [2, 4]]]
# by CT

listácska = [1, 2, [3, 4], 1, [1, [2, 4]]]


def list_add(a):
    if len(a) == 0:
        return 0

    elif type(a[0]) == list:
        return list_add(a[0]) + list_add(a[1:])
    else:
        return a[0] + list_add(a[1:])


print(list_add(listácska))˛rrfzt ztlkl
