

def maxSubarraySumCircular(nums: list[int]) -> int:
    curr_max = 0
    arr_max = nums[0]
    curr_min = 0
    arr_min = nums[0]
    total = 0
    
    for i in nums:
        total += i
        curr_max = max(curr_max+i, i)
        arr_max = max(arr_max, curr_max)

        curr_min = min(curr_min+i, i)
        arr_min = min(arr_min, curr_min)
        
        
    if total-arr_min == 0:
        return arr_max
    return max(arr_max, total-arr_min)


nums = [-3,-2,-3]
print(maxSubarraySumCircular(nums))