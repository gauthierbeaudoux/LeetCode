
def minimumDeletions(nums: list[int]) -> int:
    n = len(nums)
    
    id_min = 0
    mini = nums[0]
    id_max = 0
    maxi = nums[0]
    
    for i, val in enumerate(nums):
        if val > maxi:
            maxi = val
            id_max = i
        if val < mini:
            mini = val
            id_min = i
            
    id_g = min(id_min, id_max)
    id_d = max(id_min, id_max)

    return min(1+id_d, n-id_g, id_g+1 + n-id_d) 


nums = [2,10,7,5,4,1,8,6]
print(minimumDeletions(nums))