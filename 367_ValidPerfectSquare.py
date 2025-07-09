num = 16


def main(num):
    l = 0
    r = num
    while r >= l:
        m = (l+r)//2
        if m**2 == num:
            return True
        elif m**2 > num:
            r = m-1
        else:
            l = m+1
    return False
    
print(main(num))