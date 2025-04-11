low = 99
high = 1782


def countSymmetricIntegers(low: int, high: int) -> int:
    result = 0
    str_low = str(low)
    n = len(str_low)
    if n % 2 == 1:
        m = 10**n
    else:
        m = low
    
    # print(m)
    n = len(str(m))
    while m <= high:
        if len(str(m)) == n:
            gauche = str(m)[:n//2]
            droite = str(m)[n//2:]
            # print(gauche)
            # print(droite)
            r_g = 0
            for i in gauche:
                r_g += int(i)
            r_d = 0
            for i in droite:
                r_d += int(i)
            if r_g == r_d:
                # print(m)
                result += 1
        
            m += 1
        else:
            m = 10**(n+1)
            n = len(str(m))
    
    return result
    
    

print(countSymmetricIntegers(low, high))