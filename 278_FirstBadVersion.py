n = 5


def main(n):
    l = 1
    r = n
    while r >= l:
        m = (l+r)//2
        result = isBadVersion(m)
        if result:
            output = m
            r = m-1
        else:
            l = m+1
    return output
    
print(main(n))