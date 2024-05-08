score = [10,3,8,9,4]

def findRelativeRanks(score: list[int]) -> list[str]:
    n = len(score)
    trie = sorted(score, reverse=True)
    result = [""]*n
    for i in range(n):
        val = trie[i]
        indice = score.index(val)
        if i == 0:
            result[indice] = "Gold Medal"
        elif i == 1:
            result[indice] = "Silver Medal"
        elif i == 2:
            result[indice] = "Bronze Medal"
        else:
            result[indice] = str(i+1)
    return result

print(findRelativeRanks(score))