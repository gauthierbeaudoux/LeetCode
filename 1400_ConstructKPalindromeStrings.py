from collections import Counter

s = "annabelle"
k = 2


def canConstruct(s: str, k: int) -> bool:
    occ_c = Counter(s)
    
    if k > len(s):
        return False
    
    nbr_impair = 0
    for i in occ_c.values():
        if i % 2 == 1:
            nbr_impair += 1
    
    if nbr_impair > k:
        return False
    return True


print(canConstruct(s, k))