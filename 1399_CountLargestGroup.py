n = 13

def countLargestGroup(n: int) -> int:
    dico = dict()
    for i in range(1, n+1):
        lettre = str(i)
        result = 0
        for j in lettre:
            result += int(j)
        dico[result] = dico.get(result,0) + 1
        
    maxi = max(dico.values())
    nb = 0
    for val in dico.values():
        if val == maxi:
            nb += 1
        
    return nb
        


print(countLargestGroup(n))