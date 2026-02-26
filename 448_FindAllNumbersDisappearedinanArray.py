from collections import defaultdict

def findDisappearedNumbers(nums: list[int]) -> list[int]:
    memo = defaultdict(lambda: False)
    
    for i in nums:

        if memo[i]:
            continue
    

        memo[i] = True
        
        
    res = []
    for i in range(1, len(nums)+1):
        if not memo[i]:
            res.append(i)

    return res

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))