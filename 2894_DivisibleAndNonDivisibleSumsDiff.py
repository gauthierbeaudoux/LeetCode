n = 10
m = 3


def differenceOfSums(n: int, m: int) -> int:
    s1 = 0
    s2 = 0
    for i in range(1, n+1):
        if i % m == 0:
            s1 += i
        else:
            s2 += i
            
    return s2-s1



print(differenceOfSums(n, m))