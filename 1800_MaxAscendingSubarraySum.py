nums = [10,20,30,5,10,50]

def maxAscendingSum(nums: list[int]) -> int:
    result = nums[0]
    current = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            current += nums[i]
        else:
            result = max(result, current)
            current = nums[i]
    
    result = max(result, current)
    return result

print(maxAscendingSum(nums))