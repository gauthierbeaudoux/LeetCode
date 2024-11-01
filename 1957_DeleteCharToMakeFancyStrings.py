s = "leeetcode"

def makeFancyString(s: str) -> str:
    occ = 1
    lettre_prec = ''
    indice = 0
    while indice < len(s):
        if s[indice] == lettre_prec:
            occ += 1
        else:
            occ = 1
            lettre_prec = s[indice]
            
        if occ >= 3:
            s = s[:indice] + s[indice+1:]
        else:
            indice += 1
        
    return s

print(makeFancyString(s))