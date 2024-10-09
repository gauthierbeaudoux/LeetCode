from collections import Counter

s = "()))(("

def minAddToMakeValid(s: str) -> int:
    ouvert = 0
    result = 0
    for i in s:
        if i == "(":
            ouvert += 1
        if i == ")":
            if ouvert > 0:
                ouvert -= 1
            else:
                result += 1
        
    return result + ouvert


print(minAddToMakeValid(s))