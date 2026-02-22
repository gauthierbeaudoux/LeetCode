

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    res = []
    maxi = max(nums[:k])
    res.append(maxi)
    
    for i in range(k, len(nums)):
        curr = nums[i]
        if curr >= maxi:
            maxi = curr
        elif nums[i-k] == maxi:
            maxi = max(nums[i-k+1:i+1])
        
        res.append(maxi)
    
    return res
            
        
    

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(maxSlidingWindow(nums, k))