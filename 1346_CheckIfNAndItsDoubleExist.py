arr = [-2,0,10,-19,4,6,-8]

def checkIfExist(arr: list[int]) -> bool:
    for value in arr:
        if value == 0:
            if arr.count(0) > 1:
                return True
        elif 2*value in arr:
            return True
    return False

print(checkIfExist(arr))