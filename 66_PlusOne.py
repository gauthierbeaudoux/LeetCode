digits = [1,2,3]

def plusOne(digits):
    nbr = 0
    n = len(digits)
    for i in range(n):
        nbr += digits[i]*10**(n-i-1)
    nbr += 1
    return list(map(int, list(str(nbr))))


print(plusOne(digits))