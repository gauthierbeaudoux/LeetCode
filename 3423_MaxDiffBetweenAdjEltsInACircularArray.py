nums = [1,2,4]

def maxAdjacentDistance(nums: list[int]) -> int:
    maxi = -1
    for i in range(len(nums)):
        maxi = max(maxi, abs(nums[i]-nums[(i+1) % len(nums)]))
    
    return maxi


print(maxAdjacentDistance(nums))