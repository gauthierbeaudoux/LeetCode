from math import sqrt
n = 15

def consecutiveNumbersSum(n: int) -> int:
    result = 1
    for j in range(1,n//2+1):
        # for j in range(i, n+1):
        racine_delta = sqrt(1+4*(2*n+j*(j-1)))
        # print(racine_delta)
        if racine_delta == int(racine_delta):
            m = (-1+racine_delta)/2
            # print(m)
            if m == int(m):
                result += 1
    return result

print(consecutiveNumbersSum(n))