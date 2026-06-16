from collections import deque

def processStr(s: str) -> str:
    result_queue = deque()
    way = True
    
    for i in s:
        if i == '%':
            way = not way
            
        elif i == '*':
            if len(result_queue) > 0:
                if way:
                    result_queue.pop()
                else:
                    result_queue.popleft()
                
        elif i == "#":
            result_queue.extend(result_queue)
            # if way:
            # else:
                # result_queue.extendleft(result_queue)
        
        else:
            if way:
                result_queue.append(i)
            else:
                result_queue.appendleft(i)
        
        # print(result_queue)
                
    if way:
        return "".join(result_queue)

    result_queue.reverse()
    return "".join(result_queue)


s = "%*xilt**s#"
print(processStr(s))