nums = [1,2,3,4]

def minimumOperations(nums: list[int]) -> int:
    result = 0
    for i in nums:
        if i % 3 > 0:
            result += 1
            
    return result

print(minimumOperations(nums))