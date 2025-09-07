n = 5

def sumZero(n: int) -> list[int]:
    result = []
    for i in range(n//2):
        result.append(n-i)
        result.append(i-n)
    
    if n % 2 == 1:
        result.append(0)
        
    return result


print(sumZero(n))