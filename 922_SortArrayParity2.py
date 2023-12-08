nums = [2,3]


def sortArrayByParityII(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        if i%2 == 0 and nums[i]%2 == 1:
            for j in range(i+1, len(nums)):
                if nums[j]%2 == 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
        elif i%2 == 1 and nums[i]%2 == 0:
            for j in range(i+1, len(nums)):
                if nums[j]%2 == 1:
                    nums[i], nums[j] = nums[j], nums[i]
                    break
    return nums


print(sortArrayByParityII(nums))