arr = [4,3,2,1,0]

def maxChunksToSorted(arr: list[int]) -> int:
    result = 0
    prev = -1
    for i in arr:
        if i <= prev:
            result += 1
        prev = i
    
    return result
        


print(maxChunksToSorted(arr))