nums = [10,4,-8,7]

def waysToSplitArray(nums: list[int]) -> int:
    result = 0
    left = 0
    right = sum(nums)
    for i in range(len(nums)-1):
        left += nums[i]
        right -= nums[i]
        if left >= right:
            result += 1

    return result

print(waysToSplitArray(nums))