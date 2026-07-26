
def maximumProduct(nums: list[int]) -> int:
    nums.sort(reverse=True)
    
    return nums[0]*nums[1]*nums[2]


nums = [-100,-98,-1,2,3,4]
print(maximumProduct(nums))