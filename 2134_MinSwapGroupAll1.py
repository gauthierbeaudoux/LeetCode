nums = [0,1,0,1,1,0,0]


def minSwaps(nums: list[int]) -> int:
    indice_1 = []
    for i in range(len(nums)):
        if nums[i] == 1:
            indice_1.append(i)
    print(indice_1)
    
    return result
    
print(minSwaps(nums))