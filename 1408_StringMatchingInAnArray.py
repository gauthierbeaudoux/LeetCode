words = ["leetcode","et","code"]


def stringMatching(words: list[str]) -> list[str]:
    result = []
    words.sort(key=lambda x: len(x))
    for i in range(len(words)):
        mot = words[i]
        for j in range(len(words)-1, i, -1):
            if mot in words[j]:
                result.append(mot)
                break
        
    return result


print(stringMatching(words))