nums = [2,1,3,4]

def check(nums: list[int]) -> bool:
    drop = 0
    mem = nums[0]
    for i in nums:
        if i < mem:
            drop += 1
        if drop > 1:
            return False
        mem = i
        
    if nums[0] < mem:
        drop += 1
        mem = i
    if drop > 1:
        return False
    
    return True
    
    
print(check(nums))