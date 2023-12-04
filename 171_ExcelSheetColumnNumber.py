
columnTitle = "ZY"

def titleToNumber(columnTitle: str) -> int:
    k = 0
    result = 0
    for i in reversed(columnTitle):
        result += 26**k*(ord(i)-64)
        k += 1
    return result

print(titleToNumber(columnTitle))