nums = [1,2,3,4]
n = 4
left = 1
right = 5

def rangeSum(nums: list[int], n: int, left: int, right: int) -> int:
    new_subarray = []
    for i in range(n):
        result = nums[i]
        new_subarray.append(result)
        j = i+1
        while j < n:
            result += nums[j]
            new_subarray.append(result)
            j += 1
    # print(new_subarray)
    new_subarray.sort()
    # print(new_subarray)
    return sum(new_subarray[left-1:right])
            


print(rangeSum(nums, n, left, right))