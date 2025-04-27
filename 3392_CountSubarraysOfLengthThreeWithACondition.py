nums = [1,2,1,4,1]

def countSubarrays(nums: list[int]) -> int:
    result = 0
    for i in range(len(nums)-2):
        if nums[i]+nums[i+2] == nums[i+1]/2:
            result += 1
        
    return result

print(countSubarrays(nums))