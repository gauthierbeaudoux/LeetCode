nums = [1,2,-1,-2,1,0,-1]

def maxSum(nums) -> int:
    unique = set(nums)
    result = 0
    for i, value in enumerate(unique):
        if i == 0:
            result = value
        elif result < 0:
            result = max(result, value)
        elif value > 0:
            result += value
        
    return result

print(maxSum(nums))