from collections import Counter

nums = [1,2,3,4,5]

def countBadPairs(nums: list[int]) -> int:
    result = 0
    n = len(nums)
    dico = {}
    
    for i in range(n):
        diff = i - nums[i]
        if diff in dico:
            dico[diff] += 1
        else:
            dico[diff] = 0
    
    print(dico)
    result = sum(dico.values())
    
    tot = sum([i for i in range(n)])
    
    return tot-result

print(countBadPairs(nums))