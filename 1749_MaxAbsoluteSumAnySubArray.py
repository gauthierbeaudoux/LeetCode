nums = [1,-3,2,3,-4]

def maxAbsoluteSum(nums: list[int]) -> int:
    result = 0
    result2 = 0
    current = 0
    current2 = 0
    for x in nums:
        current = max(x, current+x)
        current2 = min(x, current2+x)
        result = max(result, current)
        result2 = min(result2, current2)
    
    return max(abs(result), abs(result2))


print(maxAbsoluteSum(nums))