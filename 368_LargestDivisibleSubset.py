nums = [1,2,4,8]

def largestDivisibleSubset(nums: list[int]) -> list[int]:
    def is_divisible(L, num):
        for i in L:
            if i%num > 0:
                return False
        return True
    
    n = len(nums)
    result = [[]]*n
    max_nbr = max(nums)
    nums.remove(max_nbr)
    result[0] = [max_nbr]
    ligne = 1
    for _ in range(n-1):
        max_nbr = max(nums)
        nums.remove(max_nbr)
        for i in range(ligne):
            if is_divisible(result[i], max_nbr):
                result[i].append(max_nbr)
                break
        else:
            result[ligne] = [max_nbr]
            ligne += 1

    longueur_max = -1
    for ligne in result:
        if len(ligne) > longueur_max:
            longueur_max = len(ligne)
            resultat = ligne
    return resultat


print(largestDivisibleSubset(nums))
