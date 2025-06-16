nums = [7,1,5,4]

def maximumDifference(nums: list[int]) -> int:
    result = -1
    mini = nums[0]
    i = 0
    while i < len(nums):
        if nums[i] <= mini:
            mini = nums[i]
            i += 1
        else:
            result = max(result, nums[i] - mini)
            i += 1
        
    
    return result


print(maximumDifference(nums))