nums = [3,4,5,1,2]


def main(nums):
    # Search pivot indice
    
    l = 0
    r = len(nums)-1
    while r > l:
        m = (l+r)//2
        if nums[m] >= nums[0]:
            l = m+1
        else:
            r = m
    if nums[r] >= nums[0]:
        pivot = 0
    else:
        pivot = r
        
    return nums[pivot]


    
    
    
print(main(nums))