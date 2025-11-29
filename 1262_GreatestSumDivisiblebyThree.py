nums = [3,6,5,1,8]

def maxSumDivThree(nums: list[int]) -> int:
    result = sum(nums)
    if result % 3 == 0:
        return result

    



print(maxSumDivThree(nums))