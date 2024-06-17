c = 5

def judgeSquareSum(c: int) -> bool:
    starting_point = int(c**0.5)
    if c == 0:
        return True
    for i in range(starting_point, 0, -1):
        result = (c - i**2)**0.5
        if result == int(result):
            return True
    return False
        


print(judgeSquareSum(c))