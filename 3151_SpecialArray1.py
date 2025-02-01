nums = [4,3,1,6]

def isArraySpecial(nums: list[int]) -> bool:
    result = nums[0] % 2
    for i in range(1, len(nums)):
        if result == 0:
            result = nums[i] % 2
            if result == 0:
                return False
        else:
            result = nums[i] % 2
            if result == 1:
                return False
            
    return True
            


print(isArraySpecial(nums))