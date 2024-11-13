nums = [0,1,7,4,4,5]
lower = 3
upper = 6

def countFairPairs(nums: list[int], lower: int, upper: int) -> int:
    result = 0
    
    for indice, val in enumerate(nums[:-1]):
        # print(f"{indice = }")
        new_low = lower - val
        new_upp = upper - val
        for j in nums[indice+1:]:
            # print(f"{j = }")
            if j >= new_low and j <= new_upp:
                result += 1
        
    return result


print(countFairPairs(nums, lower, upper))