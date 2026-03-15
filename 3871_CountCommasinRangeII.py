

def countCommas(n: int) -> int:
    i = 5
    res = 0
    while i >= 1 and n < 10**(3*i):
        i -= 1

    res += (n-10**(3*i)+1)*i
    # print(res)
    
    j = i
    while j > 1:
        debut = 10**(3*j)-1
        fin = 10**(3*(j-1))-1
        # print(debut)
        # print(fin)
        res += (debut-fin)*(j-1)
        j -= 1
        
    
    return res
        


n = 1_000_000_000_000_000
print(countCommas(n))