nums = [3,9,7]
k = 5

def minOperations(nums: list[int], k: int) -> int:
    return sum(nums) % k


print(minOperations(nums, k))