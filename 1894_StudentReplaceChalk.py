chalk = [5,1,5]
k = 22

def chalkReplacer(chalk: list[int], k: int) -> int:
    somme = sum(chalk)
    n = k % somme
    for indice, valeur in enumerate(chalk):
        if n < valeur:
            return indice
        else:
            n -= valeur


print(chalkReplacer(chalk, k))