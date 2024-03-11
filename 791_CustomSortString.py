from collections import Counter

order = "cba"
s = "abcd" 

def customSortString(order: str, s: str) -> str:
    result = ""
    occ_lettre = Counter(s)
    for lettre in order:
        if lettre in s:
            result += lettre*occ_lettre[lettre]
            s = s.replace(lettre, "")
    result += s
    return result

print(customSortString(order, s))