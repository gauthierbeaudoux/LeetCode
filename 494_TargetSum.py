
def findTargetSumWays(nums: list[int], target: int) -> int:

    memo = dict()
    
    def recu(i, target):
        
        if (i,target) in memo:
            return memo[(i,target)]

        
        res = 0
        if len(nums[:i]) == 1:
            if nums[0] == target:
                res += 1
            if -1*nums[0] == target:
                res += 1
            return res
        
        memo[(i, target)] = recu(i-1, target-nums[i-1]) + recu(i-1, target+nums[i-1])
        return memo[(i, target)]


    return recu(len(nums), target)


nums = [1,1,1,1,1]
target = 3
print(findTargetSumWays(nums, target))