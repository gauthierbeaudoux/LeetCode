sentence = "i love eating burger"
searchWord = "burg"

def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    splitting = sentence.split(" ")
    n = len(searchWord)
    for i, mot in enumerate(splitting):
        if len(mot) >= n and mot[:n] == searchWord:
            return i+1
    
    return -1

print(isPrefixOfWord(sentence, searchWord))