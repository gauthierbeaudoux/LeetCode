nums = [0,0,1,1,1,0,0]
k = 0


def longestOnes(nums: list[int], k: int) -> int:
    l = 0
    r = 0
    result = 0

    while r < len(nums):
        if nums[r] == 0:
            k -= 1
    
        if k >= 0:
            result += 1
        else:
            if nums[l] == 0:
                k += 1
            l += 1
            
        r += 1

    return result
            
            


print(longestOnes(nums, k))