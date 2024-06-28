from collections import Counter

n = 5
roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]


def maximumImportance(n: int, roads: list[list[int]]) -> int:
    occurrence = dict()
    for i in range(n):
        occurrence[i] = 0
    
    for liste in roads:
        occurrence[liste[0]] += 1
        occurrence[liste[1]] += 1
    

    lf = sorted(occurrence.values())
    result = 0
    j = 1
    for i in lf:
        result += i*j
        j += 1
    return result
    
print(maximumImportance(n, roads))