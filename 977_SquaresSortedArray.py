nums = [-4,-1,0,3,10]

def sortedSquares(nums: list[int]) -> list[int]:
    result = [i**2 for i in nums]
    return sorted(result)


print(sortedSquares(nums))