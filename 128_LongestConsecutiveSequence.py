from collections import defaultdict


def longestConsecutive(nums: list[int]) -> int:
    memo_count = defaultdict(int)
    memo_alreadyin = defaultdict(lambda: False)
    res = 0
    
    for i in nums:
        if memo_alreadyin[i]:
            continue
        
        memo_count[i-1] += 1
        memo_count[i+1] += 1
        res = max(res, memo_count[i-1], memo_count[i+1])
        
        memo_alreadyin[i] = True

    return res


nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))