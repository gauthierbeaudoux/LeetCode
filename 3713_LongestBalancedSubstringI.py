s = "abbac"

from collections import Counter

def longestBalanced(s: str) -> int:
    occ = Counter(s)
    return len(occ)*min(occ.values())


print(longestBalanced(s))