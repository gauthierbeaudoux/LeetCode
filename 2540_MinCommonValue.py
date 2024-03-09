nums1 = [1,2,3]
nums2 = [2,4]

def getCommon(nums1: list[int], nums2: list[int]) -> int:
    for i in nums1:
        if i >= nums2[0] and i in nums2:
            return i
    return -1

    
print(getCommon(nums1, nums2))