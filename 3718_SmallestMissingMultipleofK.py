

def missingMultiple(nums: list[int], k: int) -> int:
    dico = set(nums)
    i = 1
    while True:
        if k*i in dico:
            i += 1
        else:
            return k*i
        
    

nums = [8,2,3,4,6]
k = 2
print(missingMultiple(nums, k))