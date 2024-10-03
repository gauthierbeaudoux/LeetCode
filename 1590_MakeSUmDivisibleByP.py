nums = [3,1,4,2]
p = 6

def minSubarray(nums: list[int], p: int) -> int:
    reste = sum(nums) % p
    if reste == 0:
        return 0
    
    i = 1
    while i < len(nums):
        j = 0
        while (j + i) <= len(nums):
            if sum(nums[j:j+i]) % p == reste:
                return i
            j += 1
        i += 1
        
    return -1


print(minSubarray(nums, p))
