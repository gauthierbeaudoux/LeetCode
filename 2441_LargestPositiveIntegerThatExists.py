nums = [-1,2,-3,3]

def findMaxK(nums: list[int]) -> int:
    k = max(nums)
    while k > 0 and len(nums) > 1:
        if -k in nums:
            return k
        else:
            nums.remove(k)
            k = max(nums)
    return -1


print(findMaxK(nums))