nums = [1,1,0,1]

def longestSubarray(nums: list[int]) -> int:
    l = 0
    result = 0
    nb_zeros = 0
    
    for i,r in enumerate(nums):
        if r == 0:
            nb_zeros += 1
        
        while nb_zeros > 1:
            if nums[l] == 0:
                nb_zeros -= 1
            l += 1
        
        result = max(result, i-l)
        
    return result
        
        

print(longestSubarray(nums))