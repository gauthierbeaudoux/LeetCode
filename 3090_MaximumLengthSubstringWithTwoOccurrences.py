from collections import defaultdict

def maximumLengthSubstring(s: str) -> int:
    dico = defaultdict(int)
    result = 0
    l = 0
    r = 0
    
    while r < len(s):
        # print(dico)
        dico[s[r]] += 1
        while dico[s[r]] > 2:
            dico[s[l]] -= 1
            l += 1
            
        result = max(result, r-l+1)
        r += 1
        
    return result



s = "aaaa"
print(maximumLengthSubstring(s))