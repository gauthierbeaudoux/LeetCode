s = "acfgbd"
k = 2
s = "lkpkxcigcs"
k = 6


def longestIdealString(s: str, k: int) -> int:
    for i in range(len(s)-1):
        if abs(ord(s[i])-ord(s[i+1])) > k:
            val1 = longestIdealString(s[:i]+s[i+1:],k)
            if i+1 < len(s)-1:
                val2 = longestIdealString(s[:i+1]+s[i+2:],k)
            else:
                val2 = 0
            break
    else:
        return len(s)

    return max(val1, val2)

print(longestIdealString(s,k))