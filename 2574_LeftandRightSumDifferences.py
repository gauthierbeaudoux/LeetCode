
def leftRightDifference(nums: list[int]) -> list[int]:
    droite = sum(nums)
    result = []
    gauche = 0
    for val in nums:
        droite -= val
        result.append(abs(gauche - droite))
        gauche += val
        
    return result


nums = [10,4,8,3]
print(leftRightDifference(nums))