from collections import defaultdict

s = "AABABBA"
k = 1

def characterReplacement(s: str, k: int) -> int:
    result = 0
    memo = defaultdict(int)
    left = 0
    
    for i, lettre in enumerate(s):
        memo[lettre] += 1
        
        while sum(memo.values()) - max(memo.values()) > k:
            memo[s[left]] -= 1
            left += 1
        
        result = max(result, i-left+1)
        
    
    return result
        
    


print(characterReplacement(s, k))