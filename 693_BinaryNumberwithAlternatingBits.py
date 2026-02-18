n = 3

def hasAlternatingBits(n: int) -> bool:
    bit_str = bin(n)[2:]
    
    if len(bit_str) == 1:
        return True
    elif len(bit_str) == 2:
        if bit_str == "11":
            return False
        return True
    
    for i in range(1, len(bit_str)-1):
        if bit_str[i-1] == bit_str[i] or bit_str[i] == bit_str[i+1]:
            return False
        
    return True


print(hasAlternatingBits(n))