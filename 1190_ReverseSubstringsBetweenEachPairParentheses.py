s = "(u(love)i)"

def reverseParentheses(s: str) -> str:
    parenthese = []
    for i, lettre in enumerate(s):
        if lettre == "(":
            parenthese.append(i)
        elif lettre == ")":
            a_inverser = s[parenthese[-1]+1:i]
            new_str = a_inverser[::-1]
            s = s[:parenthese[-1]+1] + new_str + s[i:]
            parenthese.pop(-1)
    s = s.replace("(","")
    s = s.replace(")","")
    return s


print(reverseParentheses(s))
