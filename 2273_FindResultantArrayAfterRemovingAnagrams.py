from collections import Counter

words = ["abba","baba","bbaa","cd","cd"]

def removeAnagrams(words: list[str]) -> list[str]:
    i = 1
    prec = Counter(words[0])
    while i < len(words):
        current = Counter(words[i])
        if current == prec:
            words.pop(i)
        else:
            prec = current
            i += 1
    
    return words


print(removeAnagrams(words))