words = ["leet","code"]
x = "e"


def findWordsContaining(words: list[str], x: str) -> list[int]:
    result = []
    for i, mot in enumerate(words):
        if x in mot:
            result.append(i)
            
    return result

print(findWordsContaining(words, x))