

def checkDivisibility(n: int) -> bool:
    sum_digit = 0
    prod_digit = 1
    for i in str(n):
        sum_digit += int(i)
        prod_digit *= int(i)
        
    return (n % (sum_digit + prod_digit) == 0)


n = 99
print(checkDivisibility(n))