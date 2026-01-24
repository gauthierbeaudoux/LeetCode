nums = [3,5,2,3]

def minPairSum(nums: list[int]) -> int:
    nums.sort()
    result = -1
    n = len(nums)
    for i in range(n//2):
        result = max(result, nums[i] + nums[n-1-i])
        
    return result


print(minPairSum(nums))