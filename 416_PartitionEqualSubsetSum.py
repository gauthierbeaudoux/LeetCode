nums = [2,2,1,1]

def canPartition(nums: list[int]) -> bool:
    nums.sort()
    
    a = 0
    b = len(nums)
    
    i = (a+b)//2
    
    while True:
        print(i)
        if sum(nums[:i]) == sum(nums[i:]):
            return True
        elif sum(nums[:i]) < sum(nums[i:]):
            if a == i:
                return False
            a = i
        else:
            if b == i:
                return False
            b = i
        i = (a+b)//2

    

print(canPartition(nums))