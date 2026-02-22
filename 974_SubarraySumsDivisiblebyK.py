from collections import defaultdict

def subarraysDivByK(nums: list[int], k: int) -> int:
    memo = defaultdict(int)
    memo[0] = 1
    somme = 0
    res = 0
    
    for i, val in enumerate(nums):
        somme = (somme + val)%k
        res += memo[somme]
        memo[somme] += 1
        
        
    return res

nums = [4,5,0,-2,-3,1]
k = 5
print(subarraysDivByK(nums, k))