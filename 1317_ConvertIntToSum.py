import math
n = 124


def getNoZeroIntegers(n: int) -> list[int]:
    m = n%10
    i = int(math.log10(n))
    # print(i)
    # print(m)
    if i == 0:
        return [1, n-1]
    if m == 9:
        return [10*i + m - 1, n - (10*i + m - 1)]
    return [10**i - m - 1, n - (10**i - m - 1)]


print(getNoZeroIntegers(n))
