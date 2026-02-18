s = "abcabcbb"

def lengthOfLongestSubstring(s: str) -> int:
    l = 0
    r = 0
    result = 0
    memo = {}
    
    for i,r in enumerate(s):
        memo[r] = memo.get(r, 0) + 1
        
        while memo[r] > 1:
            memo[s[l]] -= 1
            l += 1
        
        result = max(result, i-l+1)
        
    return result

print(lengthOfLongestSubstring(s))