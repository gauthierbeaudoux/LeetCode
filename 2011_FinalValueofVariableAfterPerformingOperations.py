operations = ["--X","X++","X++"]

def finalValueAfterOperations(operations: list[str]) -> int:
    result = 0
    for i in operations:
        if i == "--X" or i == "X--":
            result -= 1
        else:
            result += 1
    
    return result


print(finalValueAfterOperations(operations))