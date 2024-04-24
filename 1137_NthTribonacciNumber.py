n = 4

def tribonacci(n: int) -> int:
        L = [0, 1, 1]
        if n < 3:
            return L[n]
        for _ in range(n-2):
            new = sum(L)
            L[0], L[1], L[2] = L[1], L[2], new
        return L[2]
    
    
print(tribonacci(n))