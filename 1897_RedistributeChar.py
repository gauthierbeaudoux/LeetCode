words = ["abc","aabc","bc"]

def makeEqual(words: list[str]) -> bool:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    occurence = {}
    for i in alphabet:
        occurence[i] = 0
    for i in words:
        for j in i:
            occurence[j] += 1
    n = len(words)
    for i in occurence.values():
        if i % n != 0:
            return False
    return True


print(makeEqual(words))