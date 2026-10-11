

def sumOfSquares(nums: list[int]) -> int:
    result = 0
    
    n = len(nums)
    
    for i, val in enumerate(nums):
        if n%(i+1) == 0:
            result += val**2
            
            
    return result


nums = [1,2,3,4]
print(sumOfSquares(nums))