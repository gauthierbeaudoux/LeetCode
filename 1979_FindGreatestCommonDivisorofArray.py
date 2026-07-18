import math

def findGCD(nums: list[int]) -> int:
    mini = min(nums)
    maxi = max(nums)
    
    return math.gcd(mini,maxi)
    
    

nums = [2,5,6,9,10]
print(findGCD(nums))