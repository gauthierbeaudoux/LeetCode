words = ["e","a","b"]
groups = [0,0,1]

def getLongestSubsequence(words: list[str], groups: list[int]) -> list[str]:
    result = [words[0]]
    valeur = groups[0]
    
    for i, j in enumerate(groups):
        if j != valeur:
            valeur = j
            result.append(words[i])
            
    return result


print(getLongestSubsequence(words, groups))