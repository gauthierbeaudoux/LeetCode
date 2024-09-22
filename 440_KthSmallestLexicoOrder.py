n = 13
k = 2

def findKthNumber(n: int, k: int) -> int:
    result = [i for i in range(1, n+1)]
    result.sort(key=lambda x: str(x))
    return result[k-1]


print(findKthNumber(n, k))