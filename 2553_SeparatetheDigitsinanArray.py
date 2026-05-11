
def separateDigits(nums: list[int]) -> list[int]:
    result = []
    for i in nums:
        if i < 10:
            result.append(i)
        else:
            char = str(i)
            for j in char:
                result.append(int(j))
        
    return result



nums = [13,25,83,77]
print(separateDigits(nums))