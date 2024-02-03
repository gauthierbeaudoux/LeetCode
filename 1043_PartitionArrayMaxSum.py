arr = [1,4,1,5,7,3,6,1,9,9,3]
k = 4

def maxSumAfterPartitioning(arr: list[int], k: int) -> int:
    def dynamic_prog(arr,k):
        if arr == []:
            return 0
        elif len(arr) <= k:
            return max(arr)*len(arr)
        max_cout = -1
        for i in range(1,k+1):
            cout = max(arr[:i])*i + dynamic_prog(arr[i:],k)
            if cout > max_cout:
                max_cout = cout
        return max_cout
    return dynamic_prog(arr,k)

print(maxSumAfterPartitioning(arr,k))