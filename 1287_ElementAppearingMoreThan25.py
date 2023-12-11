from statistics import mode

arr = [1,2,2,6,6,6,6,7,10]

def findSpecialInteger(arr: list[int]) -> int:
    # n = len(arr)
    # result = 0
    # memoire = arr[0]
    # for i in arr:
    #     if i == memoire:
    #         result += 1
    #         if result/n > 0.25:
    #             return i
    #     else:
    #         memoire = i
    #         result = 1
    # return 0
    return mode(arr)

print(findSpecialInteger(arr))