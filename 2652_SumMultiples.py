
n = 10**3

def sumOfMultiples(n: int) -> int:
    # Given a positive integer n, find the sum of all integers in the range
    # [1, n] inclusive that are divisible by 3, 5, or 7.
    # result = 0
    # k = 0
    # for i in range(3,n+1):
    #     k += 1
    #     if i%3 == 0 or i%5 == 0 or i%7 == 0:
    #         result += i
    # return result, k

    result = 0
    k = 0
    for i in range(3,n+1,3):
        k += 1
        result += i
    for i in range(5,n+1,5):
        k += 1
        if not(i%3 == 0):
            result += i
    for i in range(7,n+1,7):
        k += 1
        if not(i%3==0 or i%5==0):
            result += i

    return result, k


print(sumOfMultiples(n))