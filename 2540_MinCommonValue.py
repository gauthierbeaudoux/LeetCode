

def getCommon(nums1: list[int], nums2: list[int]) -> int:
    i1 = 0
    i2 = 0

    while i1 < len(nums1) and i2 < len(nums2):
        if nums1[i1] == nums2[i2]:
            return nums1[i1]
        elif nums1[i1] > nums2[i2]:
            i2 += 1
        else:
            i1 += 1
            
    return -1


nums1 = [1,2,3]
nums2 = [2,4]
print(getCommon(nums1, nums2))