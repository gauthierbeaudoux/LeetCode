

def minSubArrayLen(target: int, nums: list[int]) -> int:
    result = len(nums) + 1
    somme = 0
    left = 0
    
    for i, valeur in enumerate(nums):
        somme += valeur
        
        while somme >= target:
            result = min(result, i-left+1)
            somme -= nums[left]
            left += 1
        
    if result == len(nums)+1:
        return 0
    return result


target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))