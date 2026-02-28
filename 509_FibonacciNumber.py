

def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    
    prev = 0
    curr = 1
    for i in range(n-1):
        prev, curr = curr, prev+curr

    return curr

n = 4
print(fib(n))