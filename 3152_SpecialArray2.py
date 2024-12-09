nums = [3,4,1,2,6]
queries = [[0,4]]

def isArraySpecial(nums: list[int], queries: list[list[int]]) -> list[bool]:
    # def check_parity(liste):
    #     for i in range(len(liste)-1):
    #         if (liste[i] + liste[i+1]) != 1:
    #             return False
    #     return True
    
    # arr_nums = [i % 2 for i in nums]
    # # print(arr_nums)
    # result = []
    # for i in queries:
    #     result.append(check_parity(arr_nums[i[0]:i[1]+1]))
    
    # return result
    
    n = len(nums)
    prefix = [0] * n  # Prefix array to count special pairs

    # Build the prefix array
    for i in range(1, n):
        prefix[i] = prefix[i - 1]
        if (nums[i - 1] % 2 == nums[i] % 2):
            prefix[i] += 1

    result = []  # Result list

    # Process each query
    for left, right in queries:
        special_count = prefix[right] - (prefix[left] if left > 0 else 0)
        result.append(special_count == 0)

    return result
    

print(isArraySpecial(nums, queries))