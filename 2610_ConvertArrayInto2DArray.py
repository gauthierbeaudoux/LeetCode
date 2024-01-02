nums = [1,3,4,1,2,3,1]


def findMatrix(nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()
    while len(nums) > 0:
        liste_temp = []
        precedent = -1
        i = 0
        while i < len(nums):
            if nums[i] != precedent:
                liste_temp.append(nums[i])
                precedent = nums[i]
                nums.pop(i)
            else:
                i += 1
        result.append(liste_temp)
    return result

print(findMatrix(nums))