nums = [3,0,1]

def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    somme = n*(n+1)//2
    somme_liste = sum(nums)
    return somme - somme_liste
    
    
print(missingNumber(nums))