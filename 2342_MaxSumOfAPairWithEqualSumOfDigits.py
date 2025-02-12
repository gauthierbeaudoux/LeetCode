nums = [18,43,36,13,7]


def maximumSum(nums: list[int]) -> int:
    result = -1
    dico = {}
    for i in nums:
        num_str = str(i)
        val = 0
        for j in num_str:
            val += int(j)
        if val in dico:
            result = max(result, dico[val]+i)
            if i > dico[val]:
                dico[val] = i
        else:
            dico[val] = i
    
    return result
        


print(maximumSum(nums))