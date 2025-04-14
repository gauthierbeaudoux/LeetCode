arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3

def countGoodTriplets(arr: list[int], a: int, b: int, c: int) -> int:
    n = len(arr)
    result = 0
    for i in range(n):
        for j in range(i+1, n):
            if abs(arr[i]-arr[j]) > a:
                continue
            for k in range(j+1, n):
                if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                    result += 1
                    
    return result


print(countGoodTriplets(arr, a, b, c))