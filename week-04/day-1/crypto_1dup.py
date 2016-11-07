# Create a method that decrypts the texts/duplicated_chars.txt

def decrypt(file_name):
    decrypted = ""
    f = open(file_name)
    for line in f:
        for i in range(0, len(line) - 1, 2):
            decrypted += line[i]
        decrypted += "\n"
    f.close()
    return(decrypted)
    
print(decrypt("texts/duplicated_chars.txt"))