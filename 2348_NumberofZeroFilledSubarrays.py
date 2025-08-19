nums = [0,0,0,2,0,0]

def zeroFilledSubarray(nums: list[int]) -> int:
    result = 0
    prec = 0
    for i in nums:
        if i == 0:
            result += (1+prec)
            prec += 1
        else:
            prec = 0
    return result
            


print(zeroFilledSubarray(nums))