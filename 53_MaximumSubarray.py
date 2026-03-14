

def maxSubArray(nums: list[int]) -> int:
    curr = -1
    res = nums[0]
    
    for i in nums:
        curr = max(curr+i, i)
        res = max(res, curr)
    
    return res


nums = [5,4,-1,7,8]
print(maxSubArray(nums))