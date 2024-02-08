n = 2

def numSquares(n: int) -> int:
    def calcul(n):
        if n == 0:
            return 0
        if n == int(n**0.5)**2:
            return 1
        cout_min = float("inf")
        for i in range(int(n**0.5),0,-1):
            result = n-i**2
            cout = 1+calcul(result)
            cout_min = min(cout, cout_min)
        return cout_min
    return calcul(n)


print(numSquares(n))