nums = [1,2,2,4]
nums = [1,2,3,4,9,6,7,8,9]

def findErrorNums(nums: list[int]) -> list[int]:
    n = len(nums)
    somme_theorique = n*(n+1)//2
    doublon = sum(nums)-sum(set(nums))
    chiffre_manquant = somme_theorique-sum(set(nums))
    return [doublon, chiffre_manquant]


print(findErrorNums(nums))