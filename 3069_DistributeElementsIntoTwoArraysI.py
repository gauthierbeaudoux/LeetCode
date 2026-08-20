
def resultArray(nums: list[int]) -> list[int]:
    l1 = [nums[0]]
    v1 = nums[0]
    l2 = [nums[1]]
    v2 = nums[1]
    
    for i in range(2, len(nums)):
        
        if v1 > v2:
            l1.append(nums[i])
            v1 = nums[i]
        else:
            l2.append(nums[i])
            v2 = nums[i]
        
        
    return l1 + l2


nums = [5,4,3,8]
print(resultArray(nums))