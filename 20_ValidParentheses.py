from collections import deque

def isValid(s: str) -> bool:
    stack = deque()
    parentheses = "()[]{}"
    for i in s:
        if stack and stack[-1]+i in parentheses:
            stack.pop()
        else:
            stack.append(i)
        
    return not stack

s = "()[]{}"
print(isValid(s))