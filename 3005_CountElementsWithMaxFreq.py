from collections import Counter

nums = [1,2,2,3,1,4]

def maxFrequencyElements(nums: list[int]) -> int:
    occ_nums = Counter(nums)
    max_occ = max(occ_nums.values())
    result = 0
    for i in occ_nums.values():
        if i == max_occ:
            result += 1
            
    return result*max_occ

print(maxFrequencyElements(nums))
        