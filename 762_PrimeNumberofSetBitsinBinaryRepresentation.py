

def countPrimeSetBits(left: int, right: int) -> int:
    def is_prime(n):
        if n == 1:
            return False
        elif n == 2:
            return True
        elif n%2 == 0:
            return False
        
        for i in range(3, int(n**.5)+1, 2):
            if n%i == 0:
                return False
            
        return True
    
    result = 0
    
    for i in range(left, right+1):
        nb_one = str(bin(i))[2:].count('1')
        
        if is_prime(nb_one):
            result += 1
        
    return result
    

left = 10
right = 1000
print(countPrimeSetBits(left, right))