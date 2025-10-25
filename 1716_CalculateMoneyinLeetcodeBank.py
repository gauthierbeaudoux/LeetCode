n = 20

def totalMoney(n: int) -> int:
    nb_semaines = n//7
    reste = n%7
    result = 0
    for i in range(nb_semaines):
        result += 28+7*i
    
    for i in range(1,reste+1):
        result += nb_semaines + i
    
    return result


print(totalMoney(n))