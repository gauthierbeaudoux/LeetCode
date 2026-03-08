

def longestPalindrome(s: str) -> str:
    def is_pal(s):
        return s == s[::-1]
    
    res = s[0]
    i = 0
    maxi = 1
    while (i + maxi) <= len(s):
        j = i + maxi + 1
        while j <= len(s):
            if is_pal(s[i:j]):
                res = s[i:j]
                maxi = j-i
            j += 1
        i += 1
                
    return res

s = "babad"
print(longestPalindrome(s))
