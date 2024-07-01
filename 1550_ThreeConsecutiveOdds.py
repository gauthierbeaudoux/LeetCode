arr = [2,6,4,1]

def threeConsecutiveOdds(arr: list[int]) -> bool:
    compteur = 0
    for i in arr:
        if i % 2 == 1:
            compteur += 1
        else:
            compteur = 0
        if compteur == 3:
            return True
    return False


print(threeConsecutiveOdds(arr))