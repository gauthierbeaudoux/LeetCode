words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]


def vowelStrings(words: list[str], queries: list[list[int]]) -> list[int]:
    voyelles = "aeiou"
    new_list = [1 if i[0] in voyelles and i[-1] in voyelles else 0 for i in words]
    cumul_list = []
    for i in range(len(words)):
        if i == 0:
            cumul_list.append(new_list[i])
        else:
            cumul_list.append(new_list[i]+cumul_list[i-1])
    
    # print(cumul_list)
    result = []
    for i in queries:
        if i[0] == 0:
            valeur = cumul_list[i[1]]
        else:
            valeur = cumul_list[i[1]] - cumul_list[i[0]-1]
        result.append(valeur)
    
    return result
    

print(vowelStrings(words, queries))