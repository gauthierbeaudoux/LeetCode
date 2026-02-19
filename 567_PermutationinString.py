from collections import defaultdict, Counter


def checkInclusion(s1: str, s2: str) -> bool:
    occ = Counter(s1)
    
    if len(s1) > len(s2):
        return False
    
    memo = Counter(s2[:len(s1)])
    right = len(s1)
    
    if memo == occ:
        return True
    
    while right < len(s2):
        left = right - len(s1)
        # print(memo)
        memo[s2[right]] += 1
        memo[s2[left]] -= 1
        
        if memo[s2[left]] == 0:
            del memo[s2[left]]
        
        if memo == occ:
            return True
        
        right += 1
    
    
    return False
    

s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion(s1, s2))