import numpy as np

spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

def successfulPairs(spells: list[int], potions: list[int], success: int) -> list[int]:
    result = []
    for i in range(len(spells)):
        ligne = spells[i]*np.array(potions)
        result.append([i >= success for i in ligne].count(True))

    return result


print(successfulPairs(spells, potions, success))