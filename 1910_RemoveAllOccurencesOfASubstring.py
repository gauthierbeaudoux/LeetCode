s = "daabcbaabcbc"
part = "abc"


def removeOccurrences(s: str, part: str) -> str:
    n = len(part)
    while part in s:
        for i in range(len(s)):
            if s[i:i+n] == part:
                s = s[:i] + s[i+n:]
                break
    
    return s

print(removeOccurrences(s, part))
