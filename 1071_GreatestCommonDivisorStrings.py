from math import gcd

str1 = "ABCABC"
str2 = "ABC"

str1 = "ABABAB"
str2 = "ABAB"

# str1 = "LEET"
# str2 = "CODE"


def gcdOfStrings(str1: str, str2: str) -> str:
    n1 = len(str1)
    n2 = len(str2)
    n = min(n1, n2)
    while n > 0:
        if n1 % n == 0 and n2 % n == 0:
            result = str1[:n]
            m1 = n1//n
            m2 = n2//n
            if str1 == m1*result and str2 == m2*result:
                return result
        n -= 1
    return ''

print(gcdOfStrings(str1, str2))

print(str1[:gcd(len(str1), len(str2))])