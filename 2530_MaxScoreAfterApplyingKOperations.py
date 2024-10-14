from math import ceil

nums = [1,10,3,3,3]
k = 3

def maxKelements(nums: list[int], k: int) -> int:
    result = 0
    nums.sort(reverse=True)
    for i in range(k):
        val = max(nums[:i+1])
        indice = nums[:i+1].index(val)
        result += val
        nums[indice] = ceil(val/3)
    
    return result

print(maxKelements(nums, k))