s = "g0"

def clearDigits(s: str) -> str:
    i = 0
    while i < len(s):
        # print(i)
        if s[i] in "0123456789":
            if len(s) == 2:
                return ""
            elif i == 1:
                s = s[i+1:]
            elif i == len(s):
                s = s[:i-1]
            else:
                s = s[:i-1] + s[i+1:]
            i -= 1
        else:
            i += 1
        # print(s)
    return s


    
    
            
    
    
            


print(clearDigits(s))