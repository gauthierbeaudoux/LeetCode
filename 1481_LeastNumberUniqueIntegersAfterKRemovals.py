from collections import Counter

arr = [5,5,4]
arr = [1]
k = 1


def findLeastNumOfUniqueInts(arr: list[int], k: int) -> int:
    occ = Counter(arr)
    occ_sort = dict(sorted(occ.items(), key=lambda x: x[1]))
    somme = 0
    for item, valeur in occ_sort.items():
        if valeur <= k:
            k -= valeur
            somme += 1
        else:
            return len(occ)-somme
    return 0



print(findLeastNumOfUniqueInts(arr,k))