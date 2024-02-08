n = 2

def numSquares(n: int) -> int:
    memoire_result = {}
    def calcul(n):
        if n == 0:
            return 0
        if n == int(n**0.5)**2:
            return 1
        if n in memoire_result.keys():
            return memoire_result[n]
        
        cout_min = float("inf")
        for i in range(int(n**0.5),0,-1):
            result = n-i**2
            cout = 1+calcul(result)
            cout_min = min(cout, cout_min)
        memoire_result[n] = cout_min
        return cout_min
    return calcul(n)


print(numSquares(n))