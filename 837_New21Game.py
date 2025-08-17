import random

n = 6
k = 1
maxPts = 10

def new21Game(n: int, k: int, maxPts: int) -> float:
    result = [0]*(n+1)
    result[0] = 1
    for i in range(1, n+1):
        for j in range(1, maxPts+1):
            if i-j >= 0 and i-j < k:
                result[i] += result[i-j]/maxPts
        
    return round(sum(result[k:]),5)


print(new21Game(n, k, maxPts))