nums = [1,3,5,4,2,6]

def isTrionic(nums: list[int]) -> bool:
    def is_strictly_increasing(arr):
        return all(x < y for x, y in zip(arr, arr[1:]))
    def is_strictly_decreasing(arr):
        return all(x > y for x, y in zip(arr, arr[1:]))
    
    n = len(nums)
    for i in range(1, n-2):
        for j in range(i+1, n-1):
            if is_strictly_increasing(nums[:i+1]) and is_strictly_decreasing(nums[i:j+1]) and is_strictly_increasing(nums[j:]):
                # print(i,j)
                return True
        
    return False


print(isTrionic(nums))