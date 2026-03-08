

def minimumIndex(capacity: list[int], itemSize: int) -> int:
    res = -1
    maxi = 101
    for i, val in enumerate(capacity):
        if val >= itemSize and val < maxi:
            res = i
            maxi = val
            
    return res
        


capacity = [1,5,3,7]
itemSize = 3
print(minimumIndex(capacity, itemSize))