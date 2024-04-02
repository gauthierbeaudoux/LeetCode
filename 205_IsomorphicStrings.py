s = "egg"
t = "add"

def isIsomorphic(s: str, t: str) -> bool:
    lettre_t = dict()
    for i, lettre in enumerate(t):
        if lettre in lettre_t.keys():
            lettre_t[lettre].append(i)
        else:
            lettre_t[lettre] = [i]
            
    lettre_s = dict()
    for i, lettre in enumerate(s):
        if lettre in lettre_s.keys():
            lettre_s[lettre].append(i)
        else:
            lettre_s[lettre] = [i]
    
    for i in lettre_s.values():
        for k,j in lettre_t.items():
            if i == j:
                del lettre_t[k]
                break
        else:
            return False
    return True

print(isIsomorphic(s,t))