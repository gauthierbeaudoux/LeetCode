

def isSubsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True
    
    curr = 0
    for i in t:
        if i == s[curr]:
            curr += 1
            if curr == len(s):
                return True
        
    return False


s = "abc"
t = "ahbgdc"
print(isSubsequence(s, t))