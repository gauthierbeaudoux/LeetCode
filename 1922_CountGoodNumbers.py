n = 4

def countGoodNumbers(n: int) -> int:
    result = 0
    current = n
    val = 100
    while current > val:
        a = val - val//2
        b = val//2
        result += 5**a*4**b
        result %= (10**9+7)
        
        current -= val
    
    a = current - current//2
    b = current//2
    result += 5**a*4**b
    result %= (10**9+7)
    
    return result
    
        


print(countGoodNumbers(n))