nums = [-1,0,3,5,9,12]
target = 13


def search(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums)-1

    while r >= l:
        print(f"{r = }")
        print(f"{l = }")
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m-1
        elif nums[m] < target:
            l = m+1
        else:
            print("Error")
    
    return -1
        
print(search(nums, target))
        
        
