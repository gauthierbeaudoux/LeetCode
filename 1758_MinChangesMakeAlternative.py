s = "0100"


def minOperations(s: str) -> int:
    list_int = list(map(int, s))
    result_1 = 0
    result_2 = 0
    for i, nbr in enumerate(list_int):
        if i%2 == 0 and nbr == 1:
            result_1 += 1
        elif i%2 == 1 and nbr == 0:
            result_1 += 1
        if i%2 == 0 and nbr == 0:
            result_2 += 1
        elif i%2 == 1 and nbr == 1:
            result_2 += 1
    return min(result_1, result_2)
        
            
print(minOperations(s))