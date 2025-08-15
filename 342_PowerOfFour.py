import math

n = 16

def isPowerOfFour(n: int) -> bool:
    test = math.log(n)/math.log(4)
    return 4**test == n


print(isPowerOfFour(n))