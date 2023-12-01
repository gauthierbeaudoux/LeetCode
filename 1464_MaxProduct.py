nums = [3,4,5,2]

def maxProduct(nums: list[int]) -> int:
    a = max(nums)
    nums.pop(nums.index(a))
    b = max(nums)
    return (a-1)*(b-1)


print(maxProduct(nums))