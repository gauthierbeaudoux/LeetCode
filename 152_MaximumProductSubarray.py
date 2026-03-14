

def maxProduct(nums: list[int]) -> int:
    max_neg = 0
    max_pos = 0
    res = nums[0]
    
    if len(nums) == 1:
        return nums[0]
    
    for i in nums:
        if i == 0:
            max_neg = 0
            max_pos = 0
            res = max(res, 0)

        elif i > 0:
            max_pos = max(i, max_pos*i)
            max_neg *= i   
        else:
            max_neg, max_pos = min(i, max_pos*i), max_neg*i
            
        res = max(res, max_pos)
    
    return res


nums = [2,-5,-2,-4,3]
print(maxProduct(nums))