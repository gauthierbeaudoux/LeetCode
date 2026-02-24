from collections import Counter

def longestPalindrome(s: str) -> int:
    occ = Counter(s)
    res = 0
    one_off = True
    for val in occ.values():
        if val % 2 == 0:
            res += val
        else:
            q = val//2
            if one_off:
                res += val
                one_off = False
            else:
                res += 2*q
    
    return res


s = "bananas"
print(longestPalindrome(s))