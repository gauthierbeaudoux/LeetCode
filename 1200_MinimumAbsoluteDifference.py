arr = [40,11,26,27,-20]

def minimumAbsDifference(arr: list[int]) -> list[list[int]]:
    arr.sort()
    mini = arr[1] - arr[0]
    result = []
    for i in range(len(arr)-1):
        dist = arr[i+1] - arr[i]
        if dist == mini:
            result.append([arr[i], arr[i+1]])
        elif dist < mini:
            result = [[arr[i], arr[i+1]]]
            mini = dist
        
    return result
            


print(minimumAbsDifference(arr))