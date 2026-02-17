nums = [0,1,1,3,3]
k = 4


def findMaxAverage(nums: list[int], k: int) -> float:
    temp = sum(nums[:k])
    result = temp/k
    for i in range(len(nums)-k):
        temp = temp - nums[i] + nums[k+i]
        result = max(result, temp/k)
    
    return result    
    
print(findMaxAverage(nums, k))