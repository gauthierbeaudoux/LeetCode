words = ["a","aba","ababa","aa"]

def countPrefixSuffixPairs(words: list[str]) -> int:
    result = 0
    
    for i in range(len(words)-1):
        mot = words[i]
        n = len(mot)
        for j in range(i+1, len(words)):
            if words[j][:n] == mot and words[j][-n:] == mot:
                result += 1
        
    return result


print(countPrefixSuffixPairs(words))
