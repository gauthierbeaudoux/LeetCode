bills = [5,5,5,10,20]

def lemonadeChange(bills: list[int]) -> bool:
    billets = []
    for i in bills:
        if i == 5:
            billets.append(5)
        elif i == 10:
            billets.append(10)
            if 5 in billets:
                billets.remove(5)
            else:
                return False
        elif i == 20:
            billets.append(20)
            valeur = 15
            if 10 in billets:
                valeur = 5
                billets.remove(10)
            
            while valeur > 0:
                if 5 in billets:
                    valeur -= 5
                    billets.remove(5)
                else:
                    return False
            
    
    return True
            


print(lemonadeChange(bills))