from collections import defaultdict

def isGood(nums: list[int]) -> bool:
    dico = defaultdict(int)
    for i in range(1, len(nums)-1):
        dico[i] = 1
    
    dico[len(nums)-1] = 2

    for i in nums:
        dico[i] -= 1
        if dico[i] < 0:
            return False
        
    if sum(dico.values()) == 0:
        return True
    return False


nums = [2, 1, 3]
print(isGood(nums))