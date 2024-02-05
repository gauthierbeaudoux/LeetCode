from collections import Counter

s = "leetcode"

def firstUniqChar(s: str) -> int:
    occ_s = Counter(s)
    for position, lettre in enumerate(s):
        if occ_s[lettre] == 1:
            return position
    return -1


print(firstUniqChar(s))