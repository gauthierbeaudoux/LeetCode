

def smallestBalancedIndex(nums: list[int]) -> int:
    sum_l = sum(nums) - nums[-1]
    prod_r = 1
    res = -1
    i = len(nums)-1

    while i > 0 and sum_l >= prod_r:
        if sum_l == prod_r:
            res = i
        
        prod_r *= nums[i]
        
        if i > 0:
            sum_l -= nums[i-1]
        else:
            sum_l = 0
            
        i -= 1
        
    
    return res


nums = [2,8,2,2,5]
print(smallestBalancedIndex(nums))