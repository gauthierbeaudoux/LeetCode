from collections import Counter

s = "leetcode"
t = "practice"

def minSteps(s: str, t: str) -> int:
    char_s = Counter(s)
    char_t = Counter(t)
    result = 0
    for char, occurence in char_t.items():
        if not (char in char_s.keys()):
            result += occurence
        elif occurence > char_s[char]:
            result += occurence - char_s[char]

    return result

print(minSteps(s,t))