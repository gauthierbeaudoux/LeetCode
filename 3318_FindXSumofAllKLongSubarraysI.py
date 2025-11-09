from collections import Counter

nums = [1,1,2,2,3,4,2,3]
k = 6
x = 2

def findXSum(nums: list[int], k: int, x: int) -> list[int]:
    result = []
    n = len(nums)
    for i in range(n-k+1):
        arr = nums[i:i+k-1]
        if i == 0:
            occ = Counter(arr)
        else:
            occ[i-1] -= 1
            occ[i+k-1] += 1
            
        


print(nums, k, x)