
def hasAllCodes(s: str, k: int) -> bool:
    memo = dict()
    
    if len(s) < 2**k:
        return False
    
    for i in range(len(s)-k+1):
        val = s[i:i+k]
        memo[val] = 1
    
    return sum(memo.values()) == 2**k


s = "00110"
k = 2
print(hasAllCodes(s, k))