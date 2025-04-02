nums = [12,6,1,2,7]

def maximumTripletValue(nums: list[int]) -> int:
    result = 0
    
    for i in range(len(nums)-2):
        a = nums[i]
        for j in range(i+1, len(nums)-1):
            b = nums[j]
            c = max(nums[j+1:])
            calcul = (a-b)*c
            result = max(calcul, result)
            
    return result


print(maximumTripletValue(nums))