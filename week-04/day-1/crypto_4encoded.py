# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    dectext = ""
    for line in f:
        for char in line:
            if char == "\n":
                dectext += "\n"
            elif ord(char) == 32:
                dectext += " "
            else:
                chardec = ord(char) - 1
                dectext += chr(chardec)
    f.close()
    return dectext
    
print(decrypt("texts/encoded_zen_lines.txt"))