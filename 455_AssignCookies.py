g = [1,2,3]
s = [1,1]

def findContentChildren(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    result = 0
    enfant = 0
    cookies = 0
    while enfant < len(g) and cookies < len(s):
        if g[enfant] <= s[cookies]:
            result += 1
            enfant += 1
            cookies += 1
        else:
            cookies += 1
    return result

print(findContentChildren(g,s))