n = 5


def main(n):
    l = 1
    r = n
    while r >= l:
        m = (l+r)//2
        if m*(m+1)//2 <= n:
            l = m+1
            result = m
        else:
            r = m-1
    return result
    
print(main(n))