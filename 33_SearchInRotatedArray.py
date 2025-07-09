nums = [3,5,1]
target = 3


def main(nums, target):
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
        decalage = 0
    else:
        pivot = r
        decalage = len(nums[pivot:])
        
    # print(f"{pivot = }")
    
    sorted_arr = nums[pivot:] + nums[:pivot]
    
    # Search the target
    l = 0
    r = len(nums)-1
    while r >= l:
        m = (l+r)//2
        if sorted_arr[m] == target:
            if target >= nums[0]:
                return m - decalage
            else:
                return m + len(nums) - decalage
        elif sorted_arr[m] > target:
            r = m-1
        else:
            l = m+1
    
    return -1
    
    
    
print(main(nums, target))