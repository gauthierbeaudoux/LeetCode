nums = [3,1,2,2,2,1,3]
k = 2


def countPairs(nums: list[int], k: int) -> int:
    result = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and i*j % k == 0:
                result += 1

    return result

print(countPairs(nums, k))