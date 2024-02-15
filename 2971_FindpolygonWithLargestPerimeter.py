nums = [1,12,1,2,5,50,3]
nums = [5,5,50]
# nums = [5,5,5]

def largestPerimeter(nums: list[int]) -> int:
    nums.sort()
    somme = sum(nums[:-1])
    i = 0
    while somme <= nums[-1-i]:
        i += 1
        somme -= nums[-1-i]
        if len(nums[:-1-i]) < 2:
            return -1
    if i == 0: return sum(nums)
    return sum(nums[:-i])
    

print(largestPerimeter(nums))