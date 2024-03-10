nums1 = [1,2,2,1]
nums2 = [2,2]

def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    result = set()
    for i in nums1:
        if i in nums2:
            result.add(i)
            
    return list(result)

print(intersection(nums1, nums2))