nums = [4,3,2,7,8,2,3,1]

def findDuplicates(nums: list[int]) -> list[int]:
    result = []
    occ = dict()
    for i in nums:
        occ[i] = occ.get(i, 0) + 1
        if occ[i] > 1:
            result.append(i)
    return result

print(findDuplicates(nums))