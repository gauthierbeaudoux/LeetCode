n = 4
time = 5


def passThePillow(n: int, time: int) -> int:
    while time > 2*(n-1):
        time -= 2*(n-1)
    result = [i for i in range(1,n+1)]
    if time > n-1:
        time -= (n-1)
        return result[-1-time]
    else:
        return result[time]

print(passThePillow(n, time))