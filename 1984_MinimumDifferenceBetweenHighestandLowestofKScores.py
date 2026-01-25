nums = [9,4,1,7]
k = 2


def minimumDifference(nums: list[int], k: int) -> int:
    nums.sort()
    result = nums[-1] - nums[0]
    for i in range(len(nums)-k+1):
        distance = nums[i+k-1] - nums[i]
        result = min(result, distance)
        
    return result

print(minimumDifference(nums, k))