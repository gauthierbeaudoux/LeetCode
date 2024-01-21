arr = [3,1,2,4]

def sumSubarrayMins(arr: list[int]) -> int:
    result = 0
    nbr_min = min(arr)
    for i in range(len(arr)):
        for j in range(i+1,len(arr)+1):
            if nbr_min in arr[i:j]:
                result += nbr_min*(len(arr)-j+1)
                break
            result += min(arr[i:j])
    return result % (10**9 + 7)

print(sumSubarrayMins(arr))