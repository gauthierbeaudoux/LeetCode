

def closestTarget(words: list[str], target: str, startIndex: int) -> int:
    n = len(words)
    result = n+1
    for i, val in enumerate(words):
        if val == target:
            result = min(result, (startIndex-i)%n, (i-startIndex)%n)
    
    if result == (n+1):
        return -1
    return result
            


words = ["hello","i","am","leetcode","hello"]
target = "hello"
startIndex = 1
print(closestTarget(words, target, startIndex))