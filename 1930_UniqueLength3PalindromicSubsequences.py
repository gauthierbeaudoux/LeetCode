s = "bbcbaba"

def countPalindromicSubsequence(s: str) -> int:
    memoire = ""
    result = 0
    i = 0
    while i < len(s):
        lettre = s[i]
        if lettre not in memoire and lettre in s[i+2:]:
            j = len(s)-1
            while s[j] != lettre:
                j -= 1
            result += len(set(s[i+1:j]))
            memoire += lettre
        i += 1
    
    return result
            
            

print(countPalindromicSubsequence(s))