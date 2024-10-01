arr = [-10,10]
k = 10

def canArrange(arr: list[int], k: int) -> bool:
    new_arr = [i % k for i in arr]
    new_arr.sort()
    # print(new_arr)
    while len(new_arr) > 0 and new_arr[0] == 0:
        new_arr.remove(0)
    
    # print(new_arr)
    if len(new_arr)%2 == 1:
        return False

    i = 0
    while i < len(new_arr)//2:
        if (new_arr[i] + new_arr[-1-i]) % k != 0:
            return False
        i += 1
        
    return True

print(canArrange(arr, k))