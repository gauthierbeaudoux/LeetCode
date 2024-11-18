code = [2,4,9,3]
k = -2

def decrypt(code: list[int], k: int) -> list[int]:
    n = len(code)
    
    if k == 0:
        return [0]*n
    elif k > 0:
        signe = 1
    else:
        signe = -1
        
    result = []
    for i in range(n):
        somme = 0
        for j in range(1,abs(k)+1):
            somme += code[(i+j*signe)%n]
        result.append(somme)
    
    return result

        
    
print(decrypt(code, k))