from collections import Counter, defaultdict

s = "10101"

def countBinarySubstrings(s: str) -> int:
    result = 0
    memo = defaultdict(int)
    prev = int(s[0])
    
    for i, valeur in enumerate(s):
        x = int(valeur)
        
        if prev != x:
            memo[x] = 0
            prev = x
        
        memo[x] += 1
        
        if memo[abs(1-x)] >= memo[x]:
            result += 1
        
            
    return result


print(countBinarySubstrings(s))