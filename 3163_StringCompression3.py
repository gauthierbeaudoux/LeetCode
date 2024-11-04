word = "aaaaaaaaaaaaaabb"

def compressedString(word: str) -> str:
    result = ""
    occ = 0
    i = 0
    lettre = word[0]
    while i < len(word):
        if word[i] == lettre and occ < 9:
            occ += 1
            i += 1
        else:
            result += str(occ) + lettre
            lettre = word[i]
            i += 1
            occ = 1
        
        
            
    result += str(occ) + lettre
    
    return result    
            

print(compressedString(word))