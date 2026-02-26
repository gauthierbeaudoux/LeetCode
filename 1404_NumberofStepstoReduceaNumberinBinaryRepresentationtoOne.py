

def numSteps(s: str) -> int:
    nb = int(s, 2)
    res = 0
    
    while nb > 1:
        if nb%2 == 0:
            nb //= 2
        else:
            nb += 1
            
        res += 1
    
    
    return res


s = "1101"
print(numSteps(s))