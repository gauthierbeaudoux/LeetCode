import math

low = 100
high = 300

low = 10
high = 1000000000
low = 1000
high = 13000


def sequentialDigits(low: int, high: int) -> list[int]:
    multiple_low = int(math.log10(low))
    liste_int = [f'{i}' for i in range(1, 10)]
    output = []
    start = liste_int[:multiple_low]
    start = int(''.join(start))
    k = 0
    while True:
        # print(k)
        start = liste_int[:multiple_low+k+1]
        start = int(''.join(start))
        # print(k)
        j = int('1'*(multiple_low+1+k))
        for i in range(9-multiple_low-k):
            valeur = start + j*i
            # print(valeur)
            if valeur > high:
                return output
            elif valeur >= low:
                output.append(valeur)
        if 9-multiple_low-k+1 <= 0:
            return output
        k += 1
        

def sequential_digits_chatgpt(low, high):
    result = []
    
    for i in range(1, 10):  # Start with 1-digit numbers
        num = i
        for j in range(i + 1, 10):
            num = num * 10 + j
            if low <= num <= high:
                result.append(num)
                
    return sorted(result)


print(sequentialDigits(low, high))