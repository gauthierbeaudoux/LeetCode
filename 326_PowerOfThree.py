from math import log

n = 129140162


def isPowerOfThree(n: int) -> bool:
    if n < 1:
        return False
    x = log(n)/log(3)
    if 3**round(x) == n:
        return True
    return False



print(isPowerOfThree(n))