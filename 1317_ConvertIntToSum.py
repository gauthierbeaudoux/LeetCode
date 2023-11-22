import math
n = 11


def getNoZeroIntegers(n: int) -> list[int]:
    i = 1
    while True:
        if not ('0' in list(str(n-i)) or '0' in (list(str(i)))):
            return [n-i, i]
        i += 1

print(getNoZeroIntegers(n))
