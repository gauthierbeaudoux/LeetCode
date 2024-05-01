word = "abcdefd"
ch = "d"

def reversePrefix(word: str, ch: str) -> str:
    for indice, lettre in enumerate(word):
        if lettre == ch:
            return word[indice::-1] + word[indice+1:]
    return word

print(reversePrefix(word, ch))