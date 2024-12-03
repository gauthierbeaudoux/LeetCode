s = "LeetcodeHelpsMeLearn"
spaces = [8,13,15]

def addSpaces(s: str, spaces: list[int]) -> str:
    j = 0
    for i in spaces:
        s = s[:i+j] + " " + s[i+j:]
        j += 1
        
    return s


print(addSpaces(s, spaces))