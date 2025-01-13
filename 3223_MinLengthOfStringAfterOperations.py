from collections import Counter

s = "abaacbcbb"

def minimumLength(s: str) -> int:
    occ_s = Counter(s)
    # print(occ_s)
    for lettre, valeur in occ_s.items():
        while valeur >= 3:
           valeur -= 2 
        occ_s[lettre] = valeur
        
    return sum(occ_s.values())

print(minimumLength(s))