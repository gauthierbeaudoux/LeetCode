values = [8,1,5,2,6]

def maxScoreSightseeingPair(values: list[int]) -> int:
    result = 0
    n = len(values)
    for i in range(n-1):
        val = values[i]
        L = []
        for j in range(n-i-1):
            L.append(values[i+j+1]-1-j)
        result = max(result, max(L)+val)
    return result

print(maxScoreSightseeingPair(values))