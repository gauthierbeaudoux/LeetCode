nums = [1,3,5,6]
target = 2



def searchInsert(nums: list, target: int) -> int:
    l = 0
    r = len(nums)-1
    
    while r >= l:
        print(f"{l = }")
        print(f"{r = }")
        m = (r+l)//2
        if nums[m] == target:
            return m
        elif nums[m] > target:
            r = m-1
        elif nums[m] < target:
            l = m+1
        else:
            print("Erreur")
    return l


print(searchInsert(nums, target))