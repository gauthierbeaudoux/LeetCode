nums = [1,2,3,4,5]
target = 5
start = 3


def getMinDistance(nums: list[int], target: int, start: int) -> int:
    left = start
    right = start
    i = 0
    
    while True:
        if left >= 0:
            if nums[left] == target:
                return i
            left -= 1
        if right < len(nums):
            if nums[right] == target:
                return i
            right += 1
        
        i += 1

print(getMinDistance(nums, target, start))