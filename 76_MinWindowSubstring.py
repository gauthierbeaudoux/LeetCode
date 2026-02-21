from collections import Counter, defaultdict


def minWindow(s: str, t: str) -> str:
    occ_t = Counter(t)
    len_result = len(s)+1 
    left = 0
    right = 0
    result = ""
    
    while right < len(s):
        # print(occ_t)
        lettre = s[right]
        if lettre in occ_t.keys():
            occ_t[lettre] -= 1
            while max(occ_t.values()) == 0:
                if right-left < len_result:
                    len_result = right-left
                    result = s[left:right+1]  
                if s[left] in occ_t.keys():
                    occ_t[s[left]] += 1
                left += 1
        
        right += 1
        
    return result


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s,t))