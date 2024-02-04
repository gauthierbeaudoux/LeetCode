from collections import Counter

s = "ADOBECODEBANC"
t = "ABC"

def minWindow(s: str, t: str) -> str:
    occ_t = Counter(t)
    occ_s = Counter(s)
    if len(t) > len(s):
        return ""
    elif len(t) == len(s):
        for lettre in occ_t.keys():
            if occ_t[lettre] != occ_s[lettre]:
                return ""
        return t
    else:
        for lettre in occ_t.keys():
            if occ_t[lettre] > occ_s[lettre]:
                return ""
        result = []
        for lettre_t in t:
            nbr_lettre = occ_s[lettre]
            i = 0
            for lettre_s in s:
                if lettre_s == lettre_t:
                    i += 1
                    result.append([1])
                if i == nbr_lettre:
                    break


print(minWindow(s,t))