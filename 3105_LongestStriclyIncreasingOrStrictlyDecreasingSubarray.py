nums = [1,9,7,1]

def longestMonotonicSubarray(nums: list[int]) -> int:
    croiss = 1
    decroiss = 1
    result = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            result = max(result, decroiss)
            croiss += 1
            decroiss = 1
        elif nums[i] < nums[i-1]:
            result = max(result, croiss)
            decroiss += 1
            croiss = 1
        else:
            result = max(result, croiss, decroiss)
            decroiss = 1
            croiss = 1
            
    
    return max(result, croiss, decroiss)
            


print(longestMonotonicSubarray(nums))