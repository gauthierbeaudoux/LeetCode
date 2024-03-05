s = "cabaabac"
s = "aabccabba"
s = "bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbcc bcbcb ccbbabbb"

def minimumLength(s: str) -> int:
    gauche = 0
    droite = len(s)-1
    while s[gauche] == s[droite] and droite > gauche:
        while s[gauche] == s[gauche+1]:
            if gauche < droite-1:
                gauche += 1
            else:
                return 0
        while s[droite] == s[droite-1] and gauche < droite:
            droite -= 1
        
        droite -= 1
        gauche += 1
    return droite-gauche+1
        
print(minimumLength(s))