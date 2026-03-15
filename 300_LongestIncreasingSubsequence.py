

def lengthOfLIS(nums: list[int]) -> int:
    
    
    def dfs(i, valeur):
        if i == len(nums)-1:
            if nums[i] > valeur:
                return 1
            return 0
        
        res = 0
        maxi = nums[i+1]+1
        for j in range(i+1, len(nums)):
            if nums[j] < maxi:
                res = max(res, 1+dfs(j, nums[j]))
                maxi = nums[j]
            
        return res
    
    return dfs(0,0)



nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))