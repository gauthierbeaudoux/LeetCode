
def maxProduct(nums: list[int]) -> int:
    max1 = nums[0]
    max2 = nums[1]
    
    if max1 < max2:
        max1, max2 = max2, max1
        
    for i in range(2, len(nums)):
        if nums[i] > max2:
            max2 = nums[i]
            if max1 < max2:
                max1, max2 = max2, max1
        
    return (max1-1)*(max2-1)

nums = [3,4,5,2]
print(maxProduct(nums))