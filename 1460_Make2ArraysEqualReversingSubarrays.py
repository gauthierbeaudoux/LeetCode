from collections import Counter

target = [1,2,3,4]
arr = [2,4,1,3]

def canBeEqual(target: list[int], arr: list[int]) -> bool:
    array1 = Counter(target)
    array2 = Counter(arr)
    if array1 == array2:
        return True
    return False

print(canBeEqual(target, arr))