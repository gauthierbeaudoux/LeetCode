nums = [-2,-1,-1,1,2,3]

def maximumCount(nums: list[int]) -> int:
    i = 0
    n = len(nums)
    while i < n and nums[i] < 0:
        i += 1
    if i == n:
        return i
    j = i
    while j < n and nums[j] == 0:
        j += 1
    if j == n:
        return i
    
    return max(i, n-j)

print(maximumCount(nums))