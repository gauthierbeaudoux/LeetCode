nums = [6,0,8,2,1,5]

def maxWidthRamp(nums: list[int]) -> int:
    result = 0
    n = len(nums)
    val = max(nums)+1
    
    for indice, valeur in enumerate(nums):
        j = n-1
        
        if n-1 - indice <= result:
            break
        
        if valeur < val:
            while j > indice and (j-indice) > result:
                if nums[j] >= valeur:
                    result = max(result, j-indice)
                    val = valeur
                    break
                j -= 1
        
    return result

print(maxWidthRamp(nums))