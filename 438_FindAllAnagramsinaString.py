from collections import Counter

def findAnagrams(s: str, p: str) -> list[int]:
    result = []
    n = len(p)
    obj = Counter(p)
    
    if len(p) > len(s):
        return []
    
    memo = Counter(s[:n])
    
    if memo == obj:
        result.append(0)
    
    for i, lettre in enumerate(s):
        if i < n:
            continue
        memo[lettre] = memo.get(lettre, 0) + 1
        memo[s[i-n]] -= 1
        
        if memo == obj:
            result.append(i-n+1)
    
    
    return result


s = "cbaebabacd"
p = "abc"
print(findAnagrams(s, p))