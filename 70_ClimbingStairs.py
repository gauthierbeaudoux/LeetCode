from math import comb

n = 3

def climbStairs(n: int) -> int:
    
    if n == 1:
        return 1
    
    prev = 1
    curr = 2
    
    for i in range(2, n):
        prev, curr = curr, prev+curr
        
    return curr

print(climbStairs(n))