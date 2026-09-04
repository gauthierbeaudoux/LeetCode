
def firstStableIndex(nums: list[int], k: int) -> int:
    maxi = nums[0]
    mini = min(nums[:])
    
    if (maxi - mini) <= k:
        return 0
    
    for i in range(1, len(nums)):
        maxi = max(maxi, nums[i])
        if mini == nums[i-1]:
            mini = min(nums[i:])
            
        if (maxi - mini) <= k:
                return i
    
    return -1


nums = [5,0,1,4]
k = 3
print(firstStableIndex(nums, k))