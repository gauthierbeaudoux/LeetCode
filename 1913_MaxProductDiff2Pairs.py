nums = [5,6,2,7,4]

def maxProductDifference(nums: list[int]) -> int:
    list_triee = sorted(nums, reverse=True)
    return list_triee[0]*list_triee[1] - list_triee[-2]*list_triee[-1]


print(maxProductDifference(nums))