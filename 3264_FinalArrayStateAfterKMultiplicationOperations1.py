nums = [2,1,3,5,6]
k = 5
multiplier = 2



def getFinalState(nums: list[int], k: int, multiplier: int) -> list[int]:
    for _ in range(k):
        mini = min(nums)
        for i in range(len(nums)):
            if nums[i] == mini:
                nums[i] *= multiplier
                break
            
    return nums
                


print(getFinalState(nums, k, multiplier))