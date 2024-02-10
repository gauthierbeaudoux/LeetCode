s = "abc"
s = "aaa"

def countSubstrings(s: str) -> int:
    def check_palindromic(s):
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                return False
        return True

    def dp(s):
        result = 1
        if len(s) == 1:
            return 1
        for i in range(2,len(s)+1):
            if check_palindromic(s[:i]):
                result += 1
        return result+dp(s[1:])
    
    def plus_rapide(s):
        n = len(s)
        result = [1]*n
        for i in range(n):
            if i > 0: result[i] += result[i-1]
            if len(s) == 1: result[i] = 1

            for j in range(i+2,len(s)+1):
                if check_palindromic(s[i:j]):
                    result[i] += 1
        return result[-1]
    
    return plus_rapide(s)


print(countSubstrings(s))