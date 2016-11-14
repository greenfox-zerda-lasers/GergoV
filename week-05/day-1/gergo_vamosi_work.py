# 1. Check if two words ar anagrams or not.

def isanagram(word1, word2):
    word1 = ''.join(word1.split())
    word2 = ''.join(word1.split())
    return sorted(word1) == sorted(word2)

def lettercount(word):
    word = word.lower()
    wordchars = []
    ldict = {}
    for i in word:
        if i.isalpha() == True:
            wordchars += i
        else:
            continue
    for i in wordchars:
        if i in ldict:
            ldict[i] += 1
        else:
            ldict[i] = 1
    return ldict
