

def smallestNumber(n: int, t: int) -> int:
    while True:
        n_str = str(n)
        product = 1
        for i in n_str:
            product *= int(i)
            
        if product % t == 0:
            return n
        
        n += 1


n = 10
t = 2
print(smallestNumber(n, t))
