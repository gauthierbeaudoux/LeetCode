nums = [1,2,0]

def firstMissingPositive(nums: list[int]) -> int:
    result = [i for i in range(1,len(nums)+2)]
    for i in nums:
        if i in result:
            result.remove(i)
    return result[0]

print(firstMissingPositive(nums))