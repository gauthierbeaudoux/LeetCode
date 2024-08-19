n = 1


def minSteps(n: int) -> int:
    result = 0
    while n % 2 == 0:
            result += 2
            n = n//2
            
    i = 3
    while n > 1:
        if n % i == 0:
            result += i
            n = n//i
        else:
            i += 2
    
    return result
            
    



print(minSteps(n))