# 8. Given a string, compute recursively a new string where all the 'x' chars have been removed.

def delx(string):
    if string == '':
        return string
    elif string[0] == 'x':
        return '' + delx(string[1:])
    else:
        return string[0] + delx(string[1:])


print(delx("Krapulaxtaxi"))
