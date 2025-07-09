nums = [10,1,10,10,10]


def main(nums):
    # Search pivot indice
    
    l = 0
    r = len(nums)-1
    while r > l:
        m = (l+r)//2
        if nums[m] == nums[0]:
            
        elif nums[m] > nums[0]:
            l = m+1
        else:
            r = m
    print(r)
    if nums[r] >= nums[0]:
        pivot = 0
    else:
        pivot = r
        
    return nums[pivot]


    
    
    
print(main(nums))