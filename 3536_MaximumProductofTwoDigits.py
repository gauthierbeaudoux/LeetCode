

def maxProduct(n: int) -> int:
    n_str = str(n)
    max1 = int(n_str[0])
    max2 = int(n_str[1])

    if len(n_str) == 2:
        return max1*max2
    
    
    if max1 < max2:
        max1, max2 = max2, max1
    
    for i in range(2, len(n_str)):
        if int(n_str[i]) > max2:
            max2 = int(n_str[i])
            if max1 < max2:
                max1, max2 = max2, max1
        
    return max1*max2

n = 313
print(maxProduct(n))