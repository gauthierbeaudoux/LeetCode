low = 3
high = 7


def countOdds(low: int, high: int) -> int:
    if high == low:
        if high % 2 == 1:
            return 1
        return 0
    
    result = 0
    if low % 2 == 1:
        result += 1
        low += 1
    if high % 2 == 1:
        result += 1
        high -= 1
    
    diff = high - low
    return int(result + max(0, diff)/2)


print(countOdds(low, high))