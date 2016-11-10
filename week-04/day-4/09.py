# 9. Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def stars(string):
    if string == "":
        return string
    else:
        return string[0] + "*" + stars(string[1:])

print(stars("Insertstarshere"))
