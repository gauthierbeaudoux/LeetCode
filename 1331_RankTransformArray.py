arr = [37,12,28,9,100,56,80,5,12]

def arrayRankTransform(arr: list[int]) -> list[int]:
    trie = sorted(set(arr))
    # print(trie)
    dico = {}
    for i, valeur in enumerate(trie):
        dico[valeur] = i+1
        
    result = [dico[i] for i in arr]
    
    return result


print(arrayRankTransform(arr))