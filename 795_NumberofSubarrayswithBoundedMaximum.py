

def numSubarrayBoundedMax(nums: list[int], left: int, right: int) -> int:
    def nb_arr_less_than_n(n):
        result = 0
        curr = 0
        
        for i in range(len(nums)):
            if nums[i] <= n:
                curr += 1
                result += curr
            else:
                curr = 0
                
        return result
            
    
    return nb_arr_less_than_n(right) - nb_arr_less_than_n(left-1)
                
            


nums = [2,1,4,3]
left = 2
right = 3
print(numSubarrayBoundedMax(nums, left, right))