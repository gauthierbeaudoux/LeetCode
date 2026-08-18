

def largestInteger(nums: list[int], k: int) -> int:
    if k == 1:
        set_unique = set()
        set_dup = set()
        for i in nums:
            if i in set_unique:
                set_dup.add(i)
                set_unique.remove(i)
            elif i in set_dup:
                pass
            else:
                set_unique.add(i)
        
        if len(set_unique) == 0:
            return -1
        return max(set_unique)
    
    if k == len(nums):
        return max(nums)
    
    if nums[0] == nums[-1]:
        return -1
    
    set_unique = set()
    set_unique.add(nums[0])
    set_unique.add(nums[-1])
    for i in range(1, len(nums)-1):
        if nums[i] in set_unique:
            set_unique.remove(nums[i])
        
    if len(set_unique) == 0:
        return -1
    return max(set_unique)
        


nums = [3,9,2,1,7]
k = 3
print(largestInteger(nums, k))