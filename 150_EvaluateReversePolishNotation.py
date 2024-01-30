tokens = ["2","1","+","3","*"]
tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

def evalRPN(tokens: list[str]) -> int:
    operateur = "+-*/"
    if len(tokens) == 1:
        return int(tokens[0])
    stack = []
    for i in range(len(tokens)):
        if tokens[i] in operateur:
            match tokens[i]:
                case "+":
                    result = stack[-2]+stack[-1]
                case "-":
                    result = stack[-2]-stack[-1]
                case "*":
                    result = stack[-2]*stack[-1]
                case "/":
                    result = int(stack[-2]/stack[-1])
            n = len(stack)
            del stack[n-2:n]
            stack.append(result)
        else:
            stack.append(int(tokens[i]))
    return stack[-1]


print(evalRPN(tokens))