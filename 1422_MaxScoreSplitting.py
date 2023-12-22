s = "011101"

def maxScore(s: str) -> int:
    result = -1
    for i in range(1,len(s)):
        a = s[:i].count('0')
        b = s[i:].count('1')
        if a+b > result:
            result = a+b
    return result

print(maxScore(s))