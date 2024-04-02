nums = [10,5,2,6]
k = 100

def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    def interne(nums, k):
        if len(nums) == 1:
            if nums[0] <= k:
                return 1
            else:
                return 0
            
        
            

print(numSubarrayProductLessThanK(nums, k))