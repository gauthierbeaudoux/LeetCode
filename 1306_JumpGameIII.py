

def canReach(arr: list[int], start: int) -> bool:
    memo = dict()
    forbid_list = set()
    n = len(arr)

    def recu(i):
        if i in memo:
            return memo[i]
        
        forbid_list.add(i)
        
        if arr[i] == 0:
            memo[i] = True
            return True
        
        if (i + arr[i]) >= n or (i + arr[i]) in forbid_list:
            result1 = False
        else:
            result1 = recu(i + arr[i])
        
        if (i - arr[i]) < 0 or (i - arr[i]) in forbid_list:
            result2 = False
        else:
            result2 = recu(i - arr[i])
        
        memo[i] = result1 or result2
        return memo[i]
    
    
    return recu(start)
        
        
arr = [3,0,2,1,2]
start = 2
print(canReach(arr, start))
