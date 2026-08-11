

def missingInteger(nums: list[int]) -> int:
    prefix_len = 1
    num_set = set(nums)

    for prev, curr in zip(nums, nums[1:]):
        if curr == prev + 1:
            prefix_len += 1
        else:
            break

    total = (nums[prefix_len - 1] + nums[0]) * prefix_len // 2
    while total in num_set:
        total += 1

    return total





nums = [14,9,6,9,7,9,10,4,9,9,4,4]
print(missingInteger(nums))