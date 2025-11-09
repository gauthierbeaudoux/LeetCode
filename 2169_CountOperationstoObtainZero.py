num1 = 2
num2 = 3

def countOperations(num1: int, num2: int) -> int:
    result = 0
    while True:
        if num1 == 0 or num2 == 0:
            return result
        elif num1 > num2:
            num1 -= num2
            result += 1
        elif num2 > num1:
            num2 -= num1
            result += 1
        else:
            return result + 1


print(countOperations(num1, num2))
