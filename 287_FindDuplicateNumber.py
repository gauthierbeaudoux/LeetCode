nums = [1,3,4,2,2]


def findDuplicate(nums: list[int]) -> int:
    occ = dict()
    for i in nums:
        occ[i] = occ.get(i, 0) + 1
        if occ[i] > 1:
            return i

print(findDuplicate(nums))