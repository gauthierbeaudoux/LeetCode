n = 5


def main(n):
    l = 1
    r = n
    while r >= l:
        m = (l+r)//2
        result = guess(m)
        if result == 0:
            return m
        elif result == -1:
            r = m-1
        else:
            l = m+1
    return result
    
print(main(n))