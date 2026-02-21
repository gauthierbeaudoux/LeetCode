from collections import deque

def backspaceCompare(s: str, t: str) -> bool:
    stack_s = deque()
    stack_t = deque()
    
    for i in s:
        if i == "#":
            if stack_s:
                stack_s.pop()
        else:
            stack_s.append(i)

    for i in t:
        if i == "#":
            if stack_t:
                stack_t.pop()
        else:
            stack_t.append(i)

    return stack_s == stack_t


s = "y#fo##f"
t = "y#f#o##f"
print(backspaceCompare(s, t))