from collections import defaultdict

def checkSubarraySum(nums: list[int], k: int) -> bool:
    memo_exist = defaultdict(int)
    memo_indice = defaultdict(int)
    memo_exist[0] = 1
    memo_indice[0] = -1
    somme = 0
    
    for i, val in enumerate(nums):
        somme += val
        if memo_exist[somme%k] == 1:
            if i-memo_indice[somme%k] >= 2:
                return True
        else:
            memo_exist[somme%k] = 1
            memo_indice[somme%k] = i
    
    return False
        


nums = [0,0]
k = 2
print(checkSubarraySum(nums, k))