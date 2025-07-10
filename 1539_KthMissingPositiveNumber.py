arr = [1,2,3,4]
k = 2


def main(arr, k):
    result = 0
    for i, val in enumerate(arr):
        if i == 0:
            pre = 0
        result += val-pre-1
        # print(f"{result = }")
        # print(f"{val = }")
        pre = val
        if result >= k:
            return val - (result-k) -1
    return arr[-1] + k-result
    
print(main(arr, k))