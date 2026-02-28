

def countBits(n: int) -> list[int]:

    memo = dict()
    res = [0]
    power_2 = 0

    for i in range(1,n+1):
        if i == 2**(power_2+1):
            power_2 += 1
            res.append(1)
            continue
        nb = i-2**power_2
        if nb in memo:
            res.append(1+memo[nb])
        else:
            count = 0   
            while nb > 0:
                nb &= (nb-1)
                count += 1
            res.append(count+1)
            memo[nb] = count+1
        
    print(memo)
    return res

n = 5
print(countBits(n))