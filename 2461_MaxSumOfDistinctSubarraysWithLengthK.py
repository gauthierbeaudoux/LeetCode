nums = [1,5,4,2,9,9,9]
k = 3

def maximumSubarraySum(nums: list[int], k: int) -> int:
    n = len(nums)
    result = 0
    for i in range(n-k+1):
        if len(nums[i:i+k]) == len(set(nums[i:i+k])):
            result = max(result, sum(nums[i:i+k]))
        
    return result


print(maximumSubarraySum(nums, k))