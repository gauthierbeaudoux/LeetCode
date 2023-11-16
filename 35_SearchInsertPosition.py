nums = [1,3,4,6]
# target = 5

# target = 2
target = 7


def searchInsert(nums: list, target: int) -> int:
    if target in nums:
        return nums.index(target)
    for i in range(len(nums)):
        if target < nums[i]:
            return i
    return len(nums)


# Par dichotomie pour O(log(n))

def searchInsert_dicho(nums: list, target: int) -> int:
    d = 0
    f = len(nums) - 1
    while d <= f:
        milieu = (d + f)//2
        if nums[milieu] < target:
            d = milieu + 1
        elif nums[milieu] > target:
            f = milieu - 1
        else:
            return milieu
    return d


print(searchInsert_dicho(nums, target))