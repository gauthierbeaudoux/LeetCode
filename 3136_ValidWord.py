word = "234Adas"

def main(word):
    if len(word) < 3:
        return False
    voyelles = "aeiou"
    consonnes = "bcdfghjklmnpqrstvwxyz"
    nbr = "0123456789"
    has_voyelle = False
    has_cons = False
    for lettre in word:
        if lettre in nbr:
            continue
        lettre_format = lettre.lower()
        if lettre_format in voyelles:
            has_voyelle = True
        elif lettre_format in consonnes:
            has_cons = True
        else:
            return False
    if has_voyelle & has_cons:
        return True
    return False
            
    
print(main(word))