nums = [1,1,2,4,9]
k = 20

def minOperations(nums: list[int], k: int) -> int:
    nums.sort()
    nb_calc = []
    i_calc = 0
    i_nums = 0
    result = 0
    print(nums)
    if nums[0] < k and nums[1] < k:
        val = nums[i_nums]*2 + nums[i_nums+1]
        print(val)
        if val < k:
            nb_calc.append(val)
            print(nb_calc)
            i_nums = 2
            result += 1
        else:
            for i in nums:
                new_result = 0
                if i < k:
                    new_result += 1
                else:
                    break
            return new_result//2
    else:
        return 1
    
    
    while i_nums < len(nums) and nums[i_nums] < k:
        result += 1
        if i_calc < len(nb_calc) and nums[i_nums] <= nb_calc[i_calc]:
            val = nums[i_nums]*2
            i_nums += 1
        else:
            val = nb_calc[i_calc]*2
            i_calc += 1
            
        print(val//2)
        
        if nums[i_nums] <= nb_calc[i_calc]:
            val += nums[i_nums]
            print(nums[i_nums])
            i_nums += 1
        else:
            val += nb_calc[i_calc]
            print(nb_calc[i_calc])
            i_calc += 1
            
        
        
        if val < k:
            nb_calc.append(val)
            print(nb_calc)
        else:
            while i_nums < len(nums) and nums[i_nums] < k:
                result += 1
                i_nums += 2
        
    return result + len(nb_calc[i_calc:])//2
        
        
        

print(minOperations(nums, k))
