nums = [1,3,4,8,7,9,3,5,1]
k = 2

def divideArray(nums: list[int], k: int) -> list[list[int]]:
    n = len(nums)
    result = []
    nums.sort()
    for i in range(0,n,3):
        L = nums[i:i+3]
        if max(L)-min(L) > k:
            return []
        result.append(L)
    return result


print(divideArray(nums,k))