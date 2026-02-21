from collections import deque

def calPoints(operations: list[str]) -> int:
    stack = deque()

    for i in operations:
        if i == "D":
            stack.append(2*stack[-1])
        elif i == "C":
            if stack:
                stack.pop()
        elif i == "+":
            if len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(i))
    
    return sum(stack)
    

ops = ["5","2","C","D","+"]
print(calPoints(ops))