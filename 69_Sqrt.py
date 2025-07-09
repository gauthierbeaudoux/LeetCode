x = 3


def main(x):
    l = 0
    r = x+1
    while r >= l:
        m = (l+r)//2
        if m**2 == x:
            return m
        elif m**2 > x:
            r = m-1
        else:
            result = m
            l = m+1
    return result
    
print(main(x))