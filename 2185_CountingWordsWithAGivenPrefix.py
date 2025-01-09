words = ["pay","attention","practice","attend"]
pref = "at"

def prefixCount(words: list[str], pref: str) -> int:
    result = 0
    n = len(pref)
    
    for mot in words:
        if mot[:n] == pref:
            result += 1    
    
    return result

print(prefixCount(words, pref))