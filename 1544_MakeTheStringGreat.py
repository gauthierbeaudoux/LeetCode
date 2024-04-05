s = "leEeetcode"
s = "abBAcC"

def makeGood(s: str) -> str:
    i = 0
    while i < len(s)-1:
        if s[i].lower() == s[i+1].lower() and s[i] != s[i+1]:
            s = s[:i] + s[i+2:]
            if i > 0:
                i -= 1
        else:
            i += 1
            
    return s
    
    
print(makeGood(s))