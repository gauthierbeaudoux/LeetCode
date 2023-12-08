nums = [3,1,2,4]

def sortArrayByParity(nums: list[int]) -> list[int]:
    # result = []
    # i = 0
    # while i < len(nums):
    #     if nums[i]%2 == 0:
    #         result.append(nums[i])
    #         nums.pop(i)
    #     else:
    #         i += 1
    # return result + nums

    return sorted(nums, key=lambda x: x%2)


print(sortArrayByParity(nums))