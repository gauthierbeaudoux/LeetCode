nums = [1,2,3,4,4,4,4,5,6,7]
k = 5

def hasIncreasingSubarrays(nums: list[int], k: int) -> bool:
    if k == 1:
        if len(nums) >= 2:
            return True
        return False
    
    for i in range(len(nums)-2*k+1):
        if all(nums[i+j] < nums[i+1+j] for j in range(k-1)) and all(nums[i+k+j] < nums[i+1+k+j] for j in range(k-1)):
            return True

    return False

        


print(hasIncreasingSubarrays(nums, k))