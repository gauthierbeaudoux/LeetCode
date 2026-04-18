

def mirrorDistance(n: int) -> int:
    lettre = str(n)
    inverse = lettre[::-1]
    return abs(n - int(inverse))

n = 25
print(mirrorDistance(n))