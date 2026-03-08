from collections import defaultdict

def wordBreak(s: str, wordDict: list[str]) -> bool:
    
    
    dp = [False]*(len(s)+1)
    dp[-1] = True
    
    for i in range(len(s)-1,-1,-1):
        for mot in wordDict:
            n = len(mot)
            if (i+n) <= len(s) and s[i:i+n] == mot:
                if dp[i+n]:
                    dp[i] = True
                    break
    return dp[0]
        

s = "applepenapple"
wordDict = ["apple","pen"]
print(wordBreak(s, wordDict))