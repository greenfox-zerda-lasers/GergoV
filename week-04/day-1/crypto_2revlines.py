# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    f = open(file_name)
    reversed = ""
    for line in f:
        for char in range(len(line)-1, -1, -1):
            if line[char] == "\n":
                continue
            else:
                reversed += (line[char])
        reversed += "\n"
    return reversed
    f.close()

print(decrypt("texts/reversed_zen_lines.txt"))