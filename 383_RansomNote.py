from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    occ = Counter(ransomNote)
    
    for lettre in magazine:
        if lettre in occ:
            occ[lettre] -= 1
            if max(occ.values()) == 0:
                return True
        
    return False


ransomNote = "aa"
magazine = "baa"
print(canConstruct(ransomNote, magazine))