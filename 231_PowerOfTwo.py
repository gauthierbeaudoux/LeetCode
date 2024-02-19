import numpy as np

n = 1

def isPowerOfTwo(n: int) -> bool:
    if n <= 0: return False
    x = np.log2(n)
    return int(x) == x


print(isPowerOfTwo(n))