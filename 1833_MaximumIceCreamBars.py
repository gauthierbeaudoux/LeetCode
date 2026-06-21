

def maxIceCream(costs: list[int], coins: int) -> int:
    costs.sort()
    
    somme = 0
    nb = 0
    for i in costs:
        somme += i
        if somme <= coins:
            nb += 1
        else:
            return nb
        
    return nb
            


costs = [1,3,2,4,1]
coins = 7
print(maxIceCream(costs, coins))