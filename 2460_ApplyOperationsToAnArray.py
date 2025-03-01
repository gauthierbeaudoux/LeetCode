nums = [1,2,2,1,1,0]

def applyOperations(nums: list[int]) -> list[int]:
    result = []
    nb = 0
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0
        
        if nums[i] != 0:
            result.append(nums[i])
        else:
            nb += 1
    
    result.append(nums[-1])
    for _ in range(nb):
        result.append(0)
    
    
    return result

print(applyOperations(nums))