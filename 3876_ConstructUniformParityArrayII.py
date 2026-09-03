

def uniformArray(nums1: list[int]) -> bool:
    one_odd = False
    mini = nums1[0]
    
    for i in nums1:
        if i < mini:
            mini = i
        if i % 2 == 1:
            one_odd = True

        
    if mini % 2 == 0:
        if one_odd:
            return False
        return True
    else:
        return True


nums1 = [2,4,7,6]
print(uniformArray(nums1))