n = 2


def compute_square(n: int):
    result = 0
    for i in str(n):
        result += int(i)**2
    return result

def isHappy(n: int) -> bool:
    L = set()
    while n not in L:
        L.add(n)
        n = compute_square(n)
        if n == 1:
            return True
    return False

print(isHappy(n))