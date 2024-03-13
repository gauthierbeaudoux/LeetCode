n = 8

def pivotInteger(n: int) -> int:
    L = [i for i in range(1, n+1)]
    debut = sum(L)
    fin = n
    i = 0
    while debut != fin:
        debut -= L[-1-i]
        fin += L[-2-i]
        i += 1
        if debut < fin:
            return -1
    return L[-1-i]

print(pivotInteger(n))