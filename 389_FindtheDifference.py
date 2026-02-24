from collections import defaultdict

def findTheDifference(s: str, t: str) -> str:
    memo = defaultdict(int)
    
    for i in s:
        memo[i] += 1
    
    
    for i in t:
        memo[i] -= 1
        
        if memo[i] < 0:
            return i



s = "abcd"
t = "abcde"
print(findTheDifference(s, t))