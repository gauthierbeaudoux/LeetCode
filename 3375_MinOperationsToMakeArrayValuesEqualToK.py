nums = [5,2,5,4,5]
k = 2

def minOperations(nums: list[int], k: int) -> int:
    result = 0
    a = set(nums)
    if min(a) < k:
        return -1
    
    for i in a:
        if i > k:
            result += 1
    
    return result


print(minOperations(nums, k))