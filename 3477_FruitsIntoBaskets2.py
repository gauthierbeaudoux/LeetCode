fruits = [4,2,5]
baskets = [3,5,4]

def numOfUnplacedFruits(fruits: list[int], baskets: list[int]) -> int:
    liste_restant = [i for i in range(len(baskets))]
    result = 0
    for i in fruits:
        for j in liste_restant:
            if i <= baskets[j]:
                liste_restant.remove(j)
                break
        else:
            result += 1
    
    return result



print(numOfUnplacedFruits(fruits, baskets))