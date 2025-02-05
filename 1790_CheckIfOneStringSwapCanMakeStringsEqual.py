s1 = "bank"
s2 = "kanb"

def areAlmostEqual(s1: str, s2: str) -> bool:
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1
            if diff == 1:
                lettre1 = s1[i]
                lettre2 = s2[i]
            elif diff == 3:
                return False
            else:
                if not (lettre1 == s2[i] and lettre2 == s1[i]):
                    return False
    if diff == 1:
        return False
    return True
                
                
                
print(areAlmostEqual(s1, s2))