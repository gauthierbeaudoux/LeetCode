nums = [0,4,3,0,4]

def specialArray(nums: list[int]) -> int:
    i = 0
    compteur = 0
    while i <= len(nums):
        for k in nums:
            if k >= i:
                compteur += 1
            if compteur > i:
                break
        if compteur == i:
            return i
        else:
            compteur = 0
            i += 1
    return -1


print(specialArray(nums))