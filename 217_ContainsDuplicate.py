from collections import defaultdict

def containsDuplicate(nums: list[int]) -> bool:
    memo = defaultdict(lambda: False)
    
    for i in nums:
        if memo[i]:
            return True
        
        memo[i] = True
    
    return False


nums = [1,2,3,1]
print(containsDuplicate(nums))