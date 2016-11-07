# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    f = open(file_name)
    output = ""
    flist = list(f)
    for i in range(len(flist), 0, -1):
        output += flist[i - 1]
    print(output)
    f.close()
    return output
    
print(decrypt("texts/reversed_zen_order.txt"))