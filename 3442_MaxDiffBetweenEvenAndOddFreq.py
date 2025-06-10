from collections import Counter

s = "ililm"

def maxDifference(s: str) -> int:
    occ = Counter(s)
    max_odd = -1
    min_even = len(s)+1
    for i in occ.values():
        if i % 2 == 0 and i < min_even:
            min_even = i
        elif i % 2 == 1 and i > max_odd:
            max_odd = i
    
    
    return max_odd - min_even
            

print(maxDifference(s))