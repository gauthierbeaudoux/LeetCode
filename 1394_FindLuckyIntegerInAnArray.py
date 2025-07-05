from collections import Counter

arr = [2,2,3,4]

def findLucky(arr: list[int]) -> int:
    occ = Counter(arr)
    result = -1
    for nb, occu in occ.items():
        if nb == occu:
            result = max(result, nb)

    return result

print(findLucky(arr))