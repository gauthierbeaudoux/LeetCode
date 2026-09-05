from collections import Counter

def firstStableIndex(nums: list[int], k: int) -> int:
    occurence = Counter(nums)
    
    maxi = nums[0]
    mini = min(occurence.keys())
    
    if (maxi - mini) <= k:
        return 0
    
    for i in range(1, len(nums)):
        maxi = max(maxi, nums[i])
        
        occurence[nums[i-1]] -= 1
        
        if occurence[mini] == 0:
            mini = min(nums[i:])
            
        if (maxi - mini) <= k:
            return i
            
    return -1


nums = [5,0,1,4]
k = 3
print(firstStableIndex(nums, k))