from collections import deque

def removeDuplicates(s: str) -> str:
    stack = deque()
    
    for i, val in enumerate(s):
        if stack and stack[-1] == val:
            stack.pop()
        else:
            stack.append(val)
            
    return "".join(stack)
        
    
    
    
s = "abbaca"
print(removeDuplicates(s))