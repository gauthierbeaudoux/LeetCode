

def countCommas(n: int) -> int:
    if n >= 1000:
        return n-1000+1
    else:
        return 0


n = 1002
print(countCommas(n))