rolls = [3,2,4,3]
mean = 4
n = 2


def missingRolls(rolls: list[int], mean: int, n: int) -> list[int]:
    m = len(rolls)
    somme = sum(rolls)
    result = mean*(m+n) - somme
    if result / n > 6 or result < 0:
        return []
    
    nbr = result//n
    if nbr < 1:
        return []

    liste_r = [nbr]*n
    
    diff = result - sum(liste_r)
    if diff == 0:
        return liste_r
    
    for i in range(diff):
        liste_r[i] = nbr + 1

    return liste_r

print(missingRolls(rolls, mean, n))