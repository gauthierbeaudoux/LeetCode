nums = [5,7,7,8,8,10]
target = 8


def main(nums, target):
    mini = -1
    maxi = -1
    
    l = 0
    r = len(nums)-1
    while r >= l:
        m = (l+r)//2
        if nums[m] == target:
            maxi = m
            mini = m
            while mini >= 1 and nums[mini-1] == target:
                mini -= 1
            while maxi+1 < len(nums) and nums[maxi+1] == target:
                maxi += 1
            return [mini, maxi]
        elif nums[m] > target:
            r = m-1
        else:
            l = m+1
    
    return [-1, -1]
    
    
print(main(nums, target))