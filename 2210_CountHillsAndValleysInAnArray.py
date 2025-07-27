nums = [2,4,1,1,6,5]

def countHillValley(nums: list[int]) -> int:
    result = 0
    for i in range(len(nums)-1):
        if i == 0:
            prec = nums[i]
        else:
            if nums[i] > prec:
                if nums[i] > nums[i+1]:
                    result += 1
                    prec = nums[i]
            elif nums[i] < prec:
                if nums[i] < nums[i+1]:
                    result += 1
                    prec = nums[i]
    
    return result
                


print(countHillValley(nums))