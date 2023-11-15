haystack = "sadbutsad"
needle = "sad"
# haystack = "leetcode"
# needle = "leeto"

def strStr(haystack, needle):
    n = len(needle)
    for i in range(len(haystack)):
        m = len(haystack) - i
        if m < n:
            return -1
        elif haystack[i:n+i] == needle:
            return i
    return -1


print(strStr(haystack, needle))