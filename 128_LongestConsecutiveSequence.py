from collections import defaultdict


def longestConsecutive(nums: list[int]) -> int:
    memo_count = defaultdict(int)
    memo_already_in = defaultdict(lambda : False)
    res = 0
    
    for i in nums:
        if memo_already_in[i]:
            continue
        
        res = max(res, memo_count[i]+1)
        memo_count[i-1] += 1
        memo_count[i+1] += 1
        
        memo_already_in[i] = True
        
        j = 1
        while memo_already_in[i+j]:
            j += 1
            memo_count[i+j] += 1
        j = 1
        while memo_already_in[i-j]:
            j += 1
            memo_count[i-j] += 1
            
        print(memo_count)

    return res


nums = [0,3,7,2,5,8,4,6,0,1]
print(longestConsecutive(nums))