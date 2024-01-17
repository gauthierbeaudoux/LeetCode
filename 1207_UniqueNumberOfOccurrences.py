from collections import Counter

arr = [1,2,2,1,1,3]

def uniqueOccurrences(arr: list[int]) -> bool:
    occ = Counter(arr)
    if len(occ.values()) > len(set(occ.values())):
        return False
    return True


print(uniqueOccurrences(arr))