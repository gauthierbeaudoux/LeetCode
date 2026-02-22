from collections import defaultdict

def subarraySum(nums: list[int], k: int) -> int:
    memo = defaultdict(int)
    res = 0
    somme = 0
    memo[0] = 1
    
    for i, val in enumerate(nums):
        somme += val
        res += memo[somme-k]
        memo[somme] += 1
        
    return res
            
        

nums = [-1,-1,1]
k = 0
print(subarraySum(nums, k))