

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:
    memo = dict()
    
    for i in range(len(nums)):
        val = nums[i]
        
        if val in memo:
            if i-memo[val] <= k:
                return True
        
        memo[val] = i
        
    return False


nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums, k))