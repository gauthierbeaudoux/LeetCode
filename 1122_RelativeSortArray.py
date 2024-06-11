from collections import Counter

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
    dico = Counter(arr1)
    result = []
    for i in arr2:
        for _ in range(dico[i]):
            result.append(i)
    L = []
    for i in arr1:
        if i not in arr2:
            L.append(i)
    L.sort()
    return result + L


print(relativeSortArray(arr1, arr2))