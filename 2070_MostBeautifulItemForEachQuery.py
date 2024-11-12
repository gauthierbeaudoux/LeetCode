items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]

def maximumBeauty(items: list[list[int]], queries: list[int]) -> list[int]:    
    """
    result = []
    items.sort(key=lambda x: x[0])
    # print(items)
    for value in queries:
        maxi = 0
        for i in items:
            if i[0] <= value:
                if i[1] > maxi:
                    maxi = i[1]
            else:
                break
        result.append(maxi)
    """
    
    items.sort(key=lambda x: x[0])
    dico = {}
    maxi = 0
    for i in items:
        maxi = max(maxi, i[1])
        dico[i[0]] = maxi
    # print(dico)
    
    result = []
    cles = list(dico.keys())
    # print(cles)
    for value in queries:
        if value in cles:
            result.append(dico[value])
        else:
            if value < cles[0]:
                result.append(0)
            else:
                k = -1
                while cles[k] > value:
                    k -= 1
                result.append(dico[cles[k]])
    
    
    return result
    

print(maximumBeauty(items, queries))