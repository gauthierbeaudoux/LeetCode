nums = [1,2,4,5,10]

def tupleSameProduct(nums: list[int]) -> int:
    result = 0
    for i in range(3):
        if i == 0:
            r1 = nums[0]*nums[1]
            r2 = nums[2]*nums[3]
        elif i == 1:
            r1 = nums[0]*nums[2]
            r2 = nums[3]*nums[1]
        elif i == 2:
            r1 = nums[0]*nums[3]
            r2 = nums[1]*nums[2]
            
        if r1 == r2:
            result += 8
    
    return result
        


print(tupleSameProduct(nums))