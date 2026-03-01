
def canPartition(nums: list[int]) -> bool:
    somme = sum(nums)
    
    if somme % 2 == 1:
        return False
    
    memo = dict()
    def dfs(i, target):
        if target == 0:
            return True
        if i >= len(nums) or target < 0:
            return False
        if nums[i] == target:
            return True
        
        if target in memo:
            return memo[target]
        
        memo[target] = dfs(i+1, target - nums[i]) or dfs(i+1, target)
        return memo[target]
        

    return dfs(0, somme//2)

nums = [3,3,6,8,16,16,16,18,20]
print(canPartition(nums))